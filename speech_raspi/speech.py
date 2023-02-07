import pygame
import requests
import speech_recognition as sr
url_fan = "http://192.168.1.111:8000/fan/"
url_lights = "http://192.168.1.111:8000/lights/"
def post_on(url, key):
    data = {key: 'bat'}
    response_on = requests.post(url=url, data=data)
    return response_on.status_code

def post_off(url, key):
    data = {key: 'tat'}
    response_off = requests.post(url=url, data=data)
    return response_off.status_code

def speech_recognition():
    try:
        r = sr.Recognizer() #khởi tạo nhận dạng giọng nói
        with sr.Microphone() as source:
            print("Mời bạn nói: ")
            audio = r.record(source, duration=3)
            text = r.recognize_google(audio,language="vi") # gọi đến api của gg
            text = text.lower()
            print("Bạn:  {}".format(text))
            return text
    except Exception as e:
        print(e)

def main():
    text = str(speech_recognition())
    pygame.mixer.init()
    value_fan = 'value_fan'
    value_lights = 'value_lights'
    if "bật" in text and "quạt" in text:
        post_on(url_fan, value_fan )
        print("đã bật quạt")
        pygame.mixer.music.load('batquat.mp3')
        pygame.mixer.music.play()
        # text == ""
    elif "tắt" in text and "quạt" in text:
        post_off(url_fan, value_fan)
        print(" quạt đã tắt")
        pygame.mixer.music.load('tatquat.mp3')
        pygame.mixer.music.play()
        # text == ""
    elif "tắt" in text and "đèn" in text:
        post_off(url_lights, value_lights)
        print(" đèn đã tắt")
        pygame.mixer.music.load('tatden.mp3')
        pygame.mixer.music.play()
        # text == ""
    elif "bật" in text and "đèn" in text:
        post_off(url_lights, value_lights)
        print(" đèn đã được bật")
        pygame.mixer.music.load('batden.mp3')
        pygame.mixer.music.play()
        # text == ""


if __name__ == "__main__":
    while True:
        main()