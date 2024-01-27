import openai
import gradio as gr
import TTS
import whisperousf.whisper as whisper
import numpy as np

tts = TTS.TTS()
tts.load_model(engine="tts", lang="en")
wh = whisper.Whisper()
wh.init(whisper.DeviceType.GPU, "en-US")

api_key = "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"
openai.api_key = api_key


def generate_response(text):
    # Convert text to speech
    audio = tts.get_tts(text, "female")

    # Convert speech to text
    text = wh.transcribe(audio, "en-US")

    # Generate response using GPT-3
    prompt = "Answer the following question: " + text
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1000)

    # Convert response to text
    answer = response.choices[0].text

    # Convert text to speech
    return answer


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(f"User said: {command}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"

    return command.lower()


def initialize_engine():
    engine = pyttsx3.init()
    return engine


def speak(engine, text):
    engine.say(text)
    engine.runAndWait()


def generate_response(text):
    prompt = "Answer the following question: " + text
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1000)
    answer = response.choices[0].text
    return answer