from flask import Flask, session, render_template

import os
import Chapter_07_Building_A_Webapp_Web_Development.Python_Code.swimclub as swimclub

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.get("/")
def index():
    return render_template("index.html")


def populate_data():
    if "swimmers" not in session:
        swim_files = os.listdir(swimclub.FOLDER)
        # swim_files.remove(".DS_Store")
        session["swimmers"] = {}
        for file in swim_files:
            name, *_ = swimclub.read_swim_data(file)
            if name not in session["swimmers"]:
                session["swimmers"][name] = []
            session["swimmers"][name].append(file)


@app.get("/swimmers")
def display_swimmers():
    populate_data()
    return str(sorted(session["swimmers"]))


@app.get("/files/<swimmer>")
def get_swimmers_files(swimmer):
    return str(session["swimmers"][swimmer])


if __name__ == "__main__":
    app.run(debug=True)
