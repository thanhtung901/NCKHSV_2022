import json

import pygame
import speech_recognition as sr
import requests
pygame.mixer.init()

def post_on(url, value):
    data_on = {'value_fan':value}
    response = requests.post(url, data=data_on)
    print(response.status_code)
def post_off(url, value):
    data_off = {'value_lights':value}
    response = requests.post(url, data=data_off)
    print(response.status_code)
def get_speech_data():
    r = sr.Recognizer() #khởi tạo nhận dạng giọng nói
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Mời bạn nói: ")
        audio = r.listen(source)
        with open("data_speech.wav", "wb") as output:
            output.write(audio.get_wav_data())

def specch_to_text():
    global text
    on = 'on'
    off = 'off'
    while True:
        try:
            r = sr.Recognizer() #khởi tạo nhận dạng giọng nói
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Mời bạn nói: ")
                audio = r.record(source)
                text = r.recognize_google(audio,language="vi") # gọi đến api của gg
                text = text.lower()
                print("Bạn:  {}".format(text))
        except Exception as e:
            print(e)
        if "bật" in text and "quạt" in text:
            # post_on(url, on )
            print("đã bật quạt")
        elif "tắt" in text and "quạt" in text:
            # post_off(url, off)
            print("đã tắt quạt")

if __name__ == "__main__":
    specch_to_text()