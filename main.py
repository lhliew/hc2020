from flask import Flask, render_template, request, session
import urllib.request
import base64
import random

from scipy.io import wavfile
import io
import soundfile as sf
import scipy.signal as sps
from werkzeug.datastructures import FileStorage

from test import soundtostr
from audio_to_matches import scorenmatch

app = Flask(__name__)
app.secret_key = 'super secret key'
news_articles = [
    "Parts of Australia's East coast have been hit by heavy rain, dousing some bushfires and also bringing water to some thirsty koalas.",
    "Buckingham Palace has announced that Prince Harry and Meghan will no longer use their royal titles and will not receive public funds.",
    "Donald Trump's legal team has issued its first response to the impeachment charges, describing them as a 'dangerous attack' on democracy.",
    "Forecasters have warned of severe storms in Australia's fire-hit state of Victoria, which could lead to flooding.",
    "Conor McGregor returned to the octagon in style as he beat American fan favourite in Las Vegas.",
    "Powers to prevent stalkers from contacting or approaching their victims while police investigate suspected offences come into force on Monday.",
    "Libya's warring rival factions are joining major powers in Germany in a renewed push to secure a ceasefire to halt the civil war."
]

climate_news = [
    "Parts of Australia's East coast have been hit by heavy rain, dousing some bushfires and also bringing water to some thirsty koalas.",
    "Extinction Rebellion protesters have ended a blockade at the entrances to Shell's Aberdeen headquarters.",
    "Microsoft has pledged to remove 'all of the carbon' from the environment that it has emitted since the company was founded in 1975.",
    "In business, climate change threats such as extreme weather and large scale biodiversity loss are now the top long term risks.",
    "Forecasters have warned of severe storms in Australia's fire-hit state of Victoria, which could lead to flooding.",
    "The longest United Nations climate talks on record in Madrid in December ended with a compromise deal regarding increasing the global response to curbing carbon.",
    "A major United Nations climate conference will take place in Glasgow later this year and the spotlight will fall on Scotland's efforts to deal with climate change.",
    "The United Nations has outlined it's new goals to save planet’s biodiversity, with 30% of the world’s land and seas being protected in the next decade.",
    "Two huge Chinese backed coal projects on the European Union’s doorstep are currently going ahead, ignoring severe concerns about pollution",
    "The German government has agreed to compensate fossil fuel companies in a deal to phase out hard coal in the next fifteen years."
]

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/read")
def read():
    session["sentence"]=random.choice(climate_news)
    return render_template('read.html',sentence=session["sentence"])

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
    straudio = soundtostr()
    print("CP1")
    written_og = session["sentence"]
    score, resulthtml,spokenhtml = scorenmatch(straudio,written_og)
    print ("Test works")
    message= "You tried to say"
    result = resulthtml
    score=str(score)
    return render_template('result.html',message=message,result=result,score=score,spoken=spokenhtml)

if __name__ == "__main__":
    app.run(debug=True)
