from flask import Flask, render_template, request
from textblob import TextBlob
from googletrans import Translator

app = Flask(__name__)

def translate(user_text):
    translator = Translator()
    text = translator.translate(user_text, src='kk', dest='en').text
    return text

def sentiment(response):
    blob = TextBlob(response)
    sentiment = blob.sentiment.polarity
    print(sentiment)
    if(sentiment >= 0):
        return 'positive'
    else:
        return 'negative'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form['user_text']
        response = translate(user_text)
        sentiment_text = sentiment(response)
        response_text = "Sentiment: {}".format(sentiment_text)
        return render_template('index.html', response_text=response_text)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)