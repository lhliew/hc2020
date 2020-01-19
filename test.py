import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

credential_path = "talkpal-ff3171367192.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# this function returns a string
def soundtostr():
        # Instantiates a client
    client = speech.SpeechClient()
    print("OK 1")
    # The name of the audio file to transcribe
    # file_name = os.path.join(
    #     os.path.dirname(__file__),
    #     'resources',
    #     'audio.raw')

    file_name = "newfile.wav"
    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    print("OK 2")
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        #sample_rate_hertz=44100,
        audio_channel_count=1,
        language_code='en-UK')

    # Detects speech in the audio file
    response = client.recognize(config, audio)
    testhere1 = response.results

    try:
        straudio = testhere1[0].alternatives[0].transcript
    except:
        straudio=""

    # print (straudio)
    # print(type(straudio))

    return straudio
