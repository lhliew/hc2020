from sentence_comparison import comparison
from build_html_string import *
from test import soundtostr
# import speech_recognition as sr

# r = sr.Recognizer()

# test_audio_file = sr.AudioFile('as/recognition/my_test_recording4.wav')
# with test_audio_file as source:
#     audio = r.record(source)
# text_from_audio = r.recognize_google(audio)
# print(text_from_audio)
# print(type(text_from_audio))

# written_og = "Parts of Australia's east coast have been hit by heavy rain and thunderstorms, dousing some bushfires but also bringing the threat of flooding. Some, such as this thirsty koala, have been making the most of the wet conditions."
# spoken_og = "Australia east Coast have been hit by heavy rain and thunderstorms losing some bushfires by also bringing the Threat of flooding have been making the most of these conditions"
# spoken_og = text_from_audio


# print('Percentage match: %d%%' % (comparison(written_og, spoken_og)[0]))
# print('HTML string:  ', build_html_string(written_og, spoken_og))

# input string character from the cloud API, output scores and html, in that order

def scorenmatch(straudio,written_og):
    #written_og = "Parts of Australia's east coast have been hit by heavy rain and thunderstorms"
    spoken_og = straudio

    # print('Percentage match: %d%%' % (comparison(written_og, spoken_og)[0]))
    # print('HTML string:  ', build_html_string(written_og, spoken_og))
    roundedscore = round(comparison(written_og, spoken_og)[0])
    return roundedscore, build_html_string(written_og, spoken_og), build_spoken_html(spoken_og)


#score, resultshtml = scorenmatch(soundtostr())
#print(score,resultshtml)
