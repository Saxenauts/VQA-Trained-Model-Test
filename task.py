from flask import Flask, render_template, request, redirect, jsonify
from flask_bootstrap import Bootstrap
import sys
import os
scriptpath = os.path.abspath('./python/')
sys.path.insert(0, scriptpath)
staticpath = os.path.abspath('./static/')
sys.path.insert(0, staticpath)
import predict as pdict




app = Flask(__name__)
bootstrap = Bootstrap(app)

##Declaration of variables
path = ""
ques = ""
nlp = ""
encoder = ""
model = ""
img_matrix = ""

@app.route('/', methods = ['GET'])
def initial():
    
    global nlp
    global encoder
    global model
    nlp, encoder, model = pdict.load()
    return render_template("index.html")


@app.route('/image', methods = ['POST', 'GET'])
def image():
    global img_matrix
    global path
    print (request.form['src'])
    url = request.form['src']
    #image_url = "http://127.0.0.1:5000/static/room.jpg"
    path = '.' + url[21:]
    print(path)
    
    img_matrix = pdict.image_matrix(nlp, encoder, model, path)
    print ("Image Features Loaded")
    return render_template("index.html")
    
@app.route('/ques', methods = ['GET' ,'POST'])
def take_question():
    global ques
    
    ques = request.form['ques']
    
    return jsonify(q = ques)

    
@app.route('/answer', methods = ['GET', 'POST'])
def answer():
    global ques
    
    
    answer = pdict.predict(nlp, encoder, model, ques, img_matrix)
    answer = str(answer[0])
    print (answer)
    return jsonify(ans = answer)
    
        
if __name__ == '__main__':
    app.run(debug = True)
    
    
