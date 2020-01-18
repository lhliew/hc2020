import speech_recognition as sr
import pyaudio

print(sr.__version__)

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

with mic as source:
    print("Speak!")
    r.adjust_for_ambient_noise(source, duration =1 )
    audio = r.listen(source)

print(r.recognize_google(audio))
