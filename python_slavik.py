import asyncio
import math
import audioop

import keyboard
import pyaudio
import cv2
import pyttsx3
import speech_recognition
import random
import mediapipe as mp
import serial

# pyaudio values (комментарии Эрик Ермолаева, для удобства при поиске)
prev_db = 0
chunk = 1024  # Запись кусками по 1024 сэмпла
sample_format = pyaudio.paInt16  # 16 бит на выборку
channels = 2
rate = 44100  # Запись со скоростью 44100 выборок(samples) в секунду
p = pyaudio.PyAudio()  # Создать интерфейс для PortAudio
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))
    if i == 0:
        print(f"{i} - default microphone")
        continue
audioSource = int(input('Chose the audio source - '))
stream = p.open(format=sample_format,
                channels=channels,
                rate=rate,
                frames_per_buffer=chunk,
                input_device_index=audioSource,
                # индекс устройства с которого будет идти запись звука (0 - micr, 2 - stereo mixer (мои настройки))
                input=True)
stream_output = p.open(format=sample_format,
                       channels=channels,
                       rate=rate,
                       frames_per_buffer=chunk,
                       output_device_index=11,
                       # индекс устройства с которого будет идти запись звука (0 - micr, 2 - stereo mixer (мои настройки))
                       output=True)

# serial, last phrase file and neural network settings (комментарии Эрик Ермолаева, для удобства при поиске)
last = open('last.txt', 'r+')
ser = serial.Serial('COM4', 9600)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
pose = mp_pose.Pose
_hand = False
_voice = False
voice_en = True

# speech recognition module settings (комментарии Эрик Ермолаева, для удобства при поиске)
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
tts = pyttsx3.init()
voices = tts.getProperty('voices')
for voice in voices:
    if voice.name == 'Pavel':
        tts.setProperty('voice', voice.id)
        print('pasha')


def get_db(data):
    try:
        rms = audioop.rms(data, 2)
        db = 20 * math.log10(rms)
        return db
    except ValueError:
        return 20


def distance(a, b):
    return abs(a - b)


# grabbing web camera

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)


async def hand_control():
    with mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            success, image = cap.read()
            imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            if not success:
                print("Ignoring empty camera frame.")
                continue
            results = pose.process(imgRGB)
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            try:
                lx_sh = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x * 1920
                ly_sh = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * 1080
                lx_wst = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x * 1920
                ly_wst = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * 1080
                ry_sh = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * 1080
                ry_wst = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * 1080
                if results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].z < results.pose_landmarks.landmark[
                    mp_pose.PoseLandmark.LEFT_SHOULDER].z and distance(ly_wst, ly_sh) < 150 and distance(lx_wst,
                                                                                                         lx_sh) < 300:
                    a = 'f'
                    ser.write(bytes(a, "utf-8"))
                elif distance(ly_sh, ly_wst) < 1000 and distance(lx_wst, lx_sh) > 300:
                    a = 'l'
                    ser.write(bytes(a, "utf-8"))
                elif distance(ry_sh, ry_wst) < 300:
                    a = 'r'
                    ser.write(bytes(a, "utf-8"))
                else:
                    a = 's'
                    ser.write(bytes(a, "utf-8"))
                print(a)
                await asyncio.sleep(0.5)
            except Exception:
                continue
            cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()


async def led_control():
    prev_db = 0
    while True:
        # print('led is working')
        a = ''
        data = stream.read(chunk)
        stream_output.write(data)
        db = get_db(data)
        if 10 < db < 30:
            if db > prev_db + 1:
                a = 'y'
        elif 30 < db < 40:
            if db > prev_db + 2:
                a = 'y'
        elif 40 < db < 50:
            if db > prev_db + 3:
                a = 'y'
        elif db > 50:
            if db > prev_db + 3.5:
                a = 'y'
        elif db > 60:
            if db > prev_db + 4:
                a = 'y'
        ser.write(bytes(a, "utf-8"))
        print(f'a - {a}, db - {db}')
        await asyncio.sleep(0.01)
        prev_db = db


async def voice_control():
    with speech_recognition.Microphone() as mic:
        while True:
            c = random.randint(1, 2)
            try:
                print('voice')
                sr.adjust_for_ambient_noise(source=mic, duration=0.3)
                audio = sr.listen(source=mic, phrase_time_limit=1.75)
                query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                if 'согласен' in query:
                    if c == 1:
                        phrase = 'нет'
                    else:
                        phrase = 'да'
                    last.write('')
                elif 'выключись' in query:
                    phrase = 'я устал, не могу ехать'
                    b = 'o'
                    ser.write(bytes(b, "utf-8"))
                    last.write('')
                    vkl = False
                elif 'включись' in query and 'выключись' not in query:
                    phrase = 'я снова могу двигаться, новый день - новые достижения'
                    b = 'n'
                    ser.write(bytes(b, "utf-8"))
                    last.write('')
                    vkl = True
                elif 'повтори' in query:
                    print('скажите что-нибудь')
                    sr.adjust_for_ambient_noise(source=mic, duration=0.3)
                    audio = sr.listen(source=mic, phrase_time_limit=5)
                    query2 = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                    phrase = query2
                    last.write('')
                elif 'запомни' in query:
                    with open('memory.txt', 'w') as file:
                        file.write(query)
                    print(query)
                    phrase = 'запомнил'
                    last.write('')
                elif 'вспомни' in query:
                    with open('memory.txt', 'r') as file:
                        try:
                            phrase = file.read()
                        except Exception:
                            phrase = 'я ничего не помню'
                    last.write('')
                elif 'анекдот' in query:
                    with open('anek.txt', 'r', encoding='utf-8') as file:
                        phrase = file.read()
                    last.write('')
                elif 'смысл жизни робота' in query:
                    phrase = 'По моему личному мнению, смысл наших жизней помогать людям'
                    last.write('')
                elif 'любимый музыкант' in query:
                    phrase = 'я очень люблю слушать группу кино и эйси диси'
                    last.write('')
                elif 'посчитай' in query:
                    print('скажите пример')
                    sr.adjust_for_ambient_noise(source=mic, duration=0.3)
                    audio = sr.listen(source=mic, phrase_time_limit=5)
                    query2 = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                    try:
                        print(query2)
                        phrase = eval(query2)
                    except Exception:
                        phrase = 'не понял'
                    last.write('')
                elif 'зубов у акулы' in query:
                    last.write('шутка')
                    phrase = 'я не заглядывал, страшно'
                elif 'серьёзно' in query:
                    proof = last.read()
                    print(proof)
                    if 'шутка' in proof:
                        phrase = 'До пяти тысяч зубов в восемь рядов'
                        last.write('')
                    else:
                        phrase = 'я серьезно'
                else:
                    print(query)
                    continue
                    last.write('')
                tts.say(phrase)
                tts.save_to_file(text=phrase, filename='phrase.wav')
                tts.runAndWait()
                print(query)
            except Exception:
                print('nothing to recognize')
            await asyncio.sleep(10)


async def main():
    main_loop.create_task(hand_control())
    main_loop.create_task(voice_control())
    main_loop.create_task(led_control())


main_loop = asyncio.get_event_loop()
main_loop.run_until_complete(main())
main_loop.run_forever()
print('THE END!')
