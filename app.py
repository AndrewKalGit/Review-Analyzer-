from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("review")
        sia = SentimentIntensityAnalyzer()
        quantText = sia.polarity_scores(text)
        return quantText
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
