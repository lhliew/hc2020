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

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/background_process", methods=['GET', 'POST'])
def background_process():
    if request.method == "POST":
        print("OK")
        data = request.files["audio_data"]
        file = None
        file = FileStorage(data)
        file.save('newfile.wav')
        print(data)
        return ("nothing")


#background process happening without any refreshing
@app.route('/result')
def result():

    print ("Test works")
    message="You tried to say"
    result="Your results2"
    return render_template('result.html',message=message,result=result)


if __name__ == "__main__":
    app.run(debug=True)
