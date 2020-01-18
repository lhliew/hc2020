import speech_recognition as sr
import pyaudio

print(sr.__version__)
print(sr.Microphone.list_microphone_names())

r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

with mic as source:
    print("Speak!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

print(r.recognize_google(audio))
