import os
from flask import Flask, render_template, request

__author__ = 'Süleyman'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    #hier maakt die een map aan waar die de file in opslaat
    target = os.path.join(APP_ROOT, 'audio/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        print(type(filename))
        #als het bestand een wav file is, sla het dan op in target map
        if filename.endswith('.wav'):
            destination = "/".join([target, filename])
            print(destination)
            file.save(destination)
            return render_template("complete.html")
        else:
            print("Het is geen wav file")
            return render_template("errorfile.html")


if __name__ == "__main__":
    app.run(port=4555, debug=True)