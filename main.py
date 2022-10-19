import mediapipe as mp
import cv2
import serial
import speech_recognition as sr
import pyttsx3
import time
import socket

serverMACAddress = 'B8:27:EB:16:7A:53'
port = 1
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))


left = 0
right = 0


# count distance for mediapipe
def distance(a, b):
    return abs(a - b)


# serial connection
# create speech recognizer
recognizer = sr.Recognizer()



with sr.Microphone() as mic:
    while True:
        recognizer.adjust_for_ambient_noise(source=mic, duration=0.5)  # delete ambient noise
        try:
            audio = recognizer.listen(source=mic, phrase_time_limit=2)  # listen to audio from microphone
            query = recognizer.recognize_google(audio_data=audio, language='ru-RU').lower()  # recognize text using with Google API
            print(query)  # print recognized data
            if "поискать" in query:
                text = 'speak xe-xe'
                s.send(bytes(text, 'UTF-8'))
                break
        except Exception:
            print("listening")


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
pose = mp_pose.Pose

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
                if distance(ly_sh, ly_wst) < 1000 and distance(lx_wst, lx_sh) > 300:
                    text = 'right'
                    s.send(bytes(text, 'UTF-8'))
                elif distance(ry_sh, ry_wst) < 300:
                    text = 'left'
                    s.send(bytes(text, 'UTF-8'))
            except Exception:
                continue
            cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
            # if s.recv(1024).decode('utf-8') == 'break':
            break
        cap.release()



with sr.Microphone() as mic:
    while True:
        try:
            audio = recognizer.listen(source=mic, phrase_time_limit=2)  # listen to audio from microphone
            query = recognizer.recognize_google(audio_data=audio,
                                                language='ru-RU').lower()  # recognize text using with Google API
            print(query)  # print recognized data
            if "4 + 6" in query:
                text = 'joke'
                s.send(bytes(text, 'UTF-8'))
                break
        except Exception:
            print("listening")


with sr.Microphone() as mic:
    while True:
        try:
            audio = recognizer.listen(source=mic, phrase_time_limit=2)  # listen to audio from microphone
            query = recognizer.recognize_google(audio_data=audio,
                                                language='ru-RU').lower()  # recognize text using with Google API
            print(query)  # print recognized data
            if "акул" in query:
                text = 'shark'
                s.send(bytes(text, 'UTF-8'))
                break
        except Exception:
            print("listening")


with sr.Microphone() as mic:
    while True:
        try:
            audio = recognizer.listen(source=mic, phrase_time_limit=2)  # listen to audio from microphone
            query = recognizer.recognize_google(audio_data=audio,
                                                language='ru-RU').lower()  # recognize text using with Google API
            print(query)  # print recognized data
            if "музыку" in query:
                text = 'music'
                s.send(bytes(text, 'UTF-8'))
                break
        except Exception:
            print("listening")


with sr.Microphone() as mic:
    while True:
        try:
            audio = recognizer.listen(source=mic, phrase_time_limit=2)  # listen to audio from microphone
            query = recognizer.recognize_google(audio_data=audio,
                                                language='ru-RU').lower()  # recognize text using with Google API
            print(query)  # print recognized data
            if "100 + 50" in query:
                text = '150'
                s.send(bytes(text, 'UTF-8'))
                break
        except Exception:
            print("listening")


with sr.Microphone() as mic:
    while True:
        try:
            audio = recognizer.listen(source=mic, phrase_time_limit=2)  # listen to audio from microphone
            query = recognizer.recognize_google(audio_data=audio,
                                                language='ru-RU').lower()  # recognize text using with Google API
            print(query)  # print recognized data
            if "умеет" in query:
                text = 'deal'
                s.send(bytes(text, 'UTF-8'))
                break
        except Exception:
            print("listening")


with sr.Microphone() as mic:
    while True:
        try:
            audio = recognizer.listen(source=mic, phrase_time_limit=2)  # listen to audio from microphone
            query = recognizer.recognize_google(audio_data=audio,
                                                language='ru-RU').lower()  # recognize text using with Google API
            print(query)  # print recognized data
            if "покупаю обоих" in query:
                text = 'yellow'
                s.send(bytes(text, 'UTF-8'))
                break
        except Exception:
            print("listening")