import subprocess
import multiprocessing
import socket
import time
import pyttsx3
import serial
# import os

# Функция для воспроизведения видео в субпроцессе


def play(file_name):
    active = multiprocessing.active_children()
    for child in active:
        child.terminate()

    subprocess.call(f'{file_name}', shell=True)


baddr = 'B0:7D:64:DD:37:A8'
channel = 1
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((baddr, channel))
s.listen(1)

ser = serial.Serial('/dev/ttyUSB0', 9600)

ser.write(bytes('b', 'utf-8`'))
pyttsx3.init()

try:
    play('animation.mp4')
    client, address = s.accept()
    while 1:
        data = client.recv(1024).decode('utf-8')
        if data == 'speak xe-xe':
            pyttsx3.speak('хе хе')
        if data == 'left' or data == 'right':
            ser.write(bytes('l', 'utf-8`'))
            time.sleep(2)
            ser.write(bytes('i', 'utf-8'))
        if data == 'joke':
            ser.write(bytes('s', 'utf-8'))
            pyttsx3.speak('Заходит улитка в бар...')
            play('glad.mp4')
        if data == 'shark':
            pyttsx3.speak('Не заглядывал, страшно')
        if data == 'music':
            play('angry.mp4')

            pyttsx3.speak('Нет, я ужасный робот, и музыкальные вкусы у нас не сходятся')
            ser.write(bytes('b', 'utf-8'))
            ser.write(bytes('q', 'utf-8'))  # blink
        if data == '150':
            play('error.mp4')
            pyttsx3.speak('150')
            time.sleep(3)
            pyttsx3.speak('Слушайте.. Ну вот зачем Вам я? Купите лучше Эрика, он сможет сделать Вам еще хоть 1000 \
            таких роботов.')
            time.sleep(3)
            pyttsx3.speak('Но Эрик же может сделать много роботов! И еда для Эрика дешевле электричества!')
        if data == 'yellow':
            ser.write(bytes('y', 'utf-8'))
            play('sad.mp4')

except:
    print("Closing socket")
    client.close()
    s.close()
