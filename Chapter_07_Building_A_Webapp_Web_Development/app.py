from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return "This is a placeholder for you webapp's opening page."


if __name__ == "__main__":
    app.run()
