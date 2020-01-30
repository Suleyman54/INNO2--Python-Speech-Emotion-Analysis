import os
import random
import io

from io import StringIO

import numpy as np
from flask import Flask, render_template, request, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from Ziggo.backend.backend_prediction import predict
from Ziggo.backend.audio_converter import convert
import pandas
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]
a = []
b = []
a,b = predict()

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/home", methods=['POST'])
def upload():
    #hier maakt die een map aan waar die de file in opslaat
    '''target = os.path.join(APP_ROOT, 'audio/temp/')
    print('hallo ' + target)

    if not os.path.isdir(target):
        os.mkdir(target)
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        print(type(filename))
        #als het bestand een wav file is, sla het dan op in target map
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
        convert(filename,destination,target)
        predict()'''
    return render_template("about.html")

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    file1 = open("C:/Users/wesac/Downloads/Ziggo/Ziggo/backend/txtlist/list.txt", "r")
    file_str = file1.readline()
    file_str2 = file_str[1:-1]
    print(file_str2)
    list2 = str.split(file_str2, ",")
    list_final = []
    for i in list2:
        list_final.append(float(i))

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    ys = list_final
    xs = range(len(ys))
    axis.plot(xs, ys)
    return fig

@app.route('/test')
def chartTest():
    return render_template('about.html', name = 'new_plot')

@app.route("/test2")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
    return render_template('chart.html', set=zip(values, labels, colors))

if __name__ == "__main__":
    app.debug = True
    app.run()