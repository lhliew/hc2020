from flask import Flask, render_template, request
import urllib.request
import base64
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Test works")
    url = request.args.get('a', 0, type=str)
    #urllib.request.urlretrieve(a,'test.wav')
    #print("Download link: ", url)
    audio_64_encode = url[37:]
    print(url[:100])
    print(audio_64_encode[:100])
    decoded = base64.b64decode(audio_64_encode)
    audio_result = open('decode.wav', 'wb')
    audio_result.write(decoded)
    audio_result.close()
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
