import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

credential_path = "talkpal-ff3171367192.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Instantiates a client
client = speech.SpeechClient()
print("OK 1")
# The name of the audio file to transcribe
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'resources',
#     'audio.raw')

file_name = "decode.wav"
# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)
print("OK 2")
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.OGG_OPUS,
    sample_rate_hertz=48000,
    audio_channel_count=1,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)
print(response)
for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
