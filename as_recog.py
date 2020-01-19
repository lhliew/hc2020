import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()

test_audio_file = sr.AudioFile('decode.wav')
with test_audio_file as source:
    audio = r.record(source)

print(type(audio))

print(r.recognize_google(audio))
