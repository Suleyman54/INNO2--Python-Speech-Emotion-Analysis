import json

from flask import Flask, render_template, jsonify, request
#from werkzeug.utils import secure_filename
import base64, os

import utils.audio_converter as audio_converter
import utils.backend_prediction2 as backend_prediction
import utils.wav_splitter as wav_splitter
UPLOAD_FOLDER = os.path.abspath('audio/temp_file')
app = Flask(__name__)

@app.route("/index")
@app.route("/")
def home():
    return render_template("index.html", content="Testing")


@app.route("/upload")
def upload():
    return render_template("upload.html", content="Testing")

@app.route("/results", methods=['GET', 'POST'])
def results():
    strength = 0
    if request.method == 'POST':
        EmptyFolders()
        upload_file = request.files['file']
        filename = upload_file.filename
        upload_file.save(os.path.join(UPLOAD_FOLDER, filename))
        filename_string = filename[0:-4] + '.wav'
        audio_converter.convert(UPLOAD_FOLDER)
        wav_splitter.split_wav(os.path.join(UPLOAD_FOLDER, filename_string))
        emotions = backend_prediction.predict()
        JsonEmotions = json.dumps(emotions)
        return render_template("result.html", emotions=JsonEmotions)
    emotions = {1: {0: 0.1391668035154432, 1: 0.7964834200029145, 2: 0.06434983061626554},
                2: {0: 0.00013751742802270428, 1: 0.7425724177355733, 2: 0.2572900280356407},
                3: {0: 0.019632020175777143, 1: 0.14060649648308754, 2: 0.8397614769637585},
                4: {0: 0.018558258232587832, 1: 0.8604737868445227, 2: 0.12096796929836273},
                5: {0: 0.012431997416570084, 1: 0.15321613289415836, 2: 0.8343518078327179}}
    jsonEmotions = json.dumps(emotions)

    return render_template("result.html", emotions=jsonEmotions, strengthvar=strength)
    # return "Error"

def EmptyFolders():
    fragsFolder = "audio/temp_frag"
    filesFolder = "audio/temp_file"
    for root, dirs, files in os.walk(fragsFolder):
        for file in files:
            os.remove(os.path.join(root, file))
    for root, dirs, files in os.walk(filesFolder):
        for file in files:
            os.remove(os.path.join(root, file))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)
