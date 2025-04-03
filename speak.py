import pyttsx3
import speech_recognition as sr

class Model:
    def __init__(self, mic_index=None):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.mic_index = mic_index

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def commands(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index=self.mic_index) as source:
            print(f"Listening on Mic {self.mic_index}...")
            r.energy_threshold = 200
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-us')
            print(f"You said: {query}")
        except Exception as e:
            print("Say again...")
            return "None"
        return query