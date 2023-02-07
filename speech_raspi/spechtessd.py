import requests
import speech_recognition as sr
url = "http://192.168.1.114:8000/fan/"
url_ = "http://192.168.1.114:8000/lights/"
def post_on(url, value):
    data_on = {value:'bat'}
    response = requests.post(url, data=data_on)
    return response.status_code

def post_off(url, value):
    data_off = {value:'tat'}
    response = requests.post(url, data=data_off)
    return response.status_code

def get_speech_data():
    r = sr.Recognizer() #khởi tạo nhận dạng giọng nói
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Mời bạn nói: ")
        audio = r.listen(source)
        # try:
        #     data = r.recognize_google(audio)
        # except:
        #     print("Failed to recognize")
        with open("data_speech.wav", "wb") as output:
            output.write(audio.get_wav_data())
def api_text_to_speech():
    url = 'https://api.fpt.ai/hmi/asr/general'
    payload = open('data_speech.wav', 'rb').read()
    headers = {
        'api-key': 'QcvZdbOhq4X6013i96gRxlkzOjFCy233'
    }
    response = requests.post(url=url, data=payload, headers=headers)
    data = response.json()['hypotheses']

    for user in data:
        text = user['utterance']
        text = text.lower()
    return text


def main():
    text = api_text_to_speech()
    print (text)
    value_fan = 'value_fan'
    value_lights = 'value_lights'
    # recording = sr.Recognizer()
    # with sr.Microphone() as source:
    #     recording.adjust_for_ambient_noise(source)
    #     print("Please Say something:")
    #     audio = recording.listen(source)
    #     try:
    #         text = recording.recognize_google(audio,language="vi-VN")
    #         text = text.lower()
    #         print("You said: n" + text)
    #     except Exception as e:
    #         print(e)
    if " bật " and " quạt " in text:
        if post_on(url, value_fan )==200:
            print("đã bật quạt")

    elif " tắt " and " quạt " in text:
        if post_off(url, value_fan)==200:
            print(" quạt đã tắt")
    text = ""

if __name__ == "__main__":
    while True:
        get_speech_data()
        main()