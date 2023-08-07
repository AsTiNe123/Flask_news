from flask import Flask, url_for, render_template

app = Flask(__name__)

News = [{"title" : "fbtherh", "text": "sghyjruk"}]

@app.route('/')
def index():
    return render_template("index.html", news = News)

@app.route("/news_detail/<int:id>")
def news_detail(id):
    title = News[id][title]
    text = News[id][text]
    return render_template("news_detail.html",
                           title = title,
                           text = text)


if __name__ == "__main__":
    app.run(debug = True)