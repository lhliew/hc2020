from flask import Flask, render_template, request, session
import urllib.request
import base64
import speech_recognition as sr
from scipy.io import wavfile
import io
import soundfile as sf
import scipy.signal as sps
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
print(sr.__version__)


r = sr.Recognizer()

"gdfhdfh'ggdfhdhf'"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        print("OK")
        data = request.files["audio_data"]
        file = None
        file = FileStorage(data)
        file.save('newfile.wav')
        print(data)
        message="You tried to say"
        result="Your results"
        return render_template('result.html',message=message,result=result)


#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Test works")
    url = request.args.get('a', 0, type=str)
    #urllib.request.urlretrieve(a,'test.wav')
    #print("Download link: ", url)
    audio_64_encode = url[37:]
    #print(url[:100])

    #print(audio_64_encode[:100])
    decoded = base64.b64decode(audio_64_encode)
    #print(type(decoded))

    # Your new sampling rate
    #new_rate = 44100
     # Resample data
    #number_of_samples = round(len(decoded) * float(new_rate) / 48000)
    #data = sps.resample(decoded, number_of_samples)

    print("Successfuly decoded")
    #
    # data, samplerate = sf.read(io.BytesIO(decoded))
    # print(samplerate)
    # with open('myfile.wav',mode='bx') as f:
    #     f.write(data)
    # print("Data:", type(data))
    #
    audio_result = open('decode.wav', 'wb')
    audio_result.write(decoded)
    audio_result.close()


    # wavio.write('decode.wav', decoded, 22050 ,sampwidth=2)
    # print("WAV file created")


    # print(type(decoded))
    # try:
    #
    #     test_audio_file = sr.AudioFile(decoded)
    #     with test_audio_file as source:
    #         audio = r.record(source)
    #     print("Sucess")
    #     print(type(audio))
    #
    #     print(r.recognize_google(audio))
    #
    # except Exception as e:
    #     print(e)




    #r = urllib.request.Request(url)
    #filedata = urllib.request.urlopen(r)
    #print("OK")
    # datatowrite = filedata.read()
    #
    # with open("test333.wav", 'wb') as f:
    #     f.write(datatowrite)

    return ("nothing")


if __name__ == "__main__":
    app.run(debug=True)
