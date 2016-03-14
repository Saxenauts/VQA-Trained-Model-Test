from flask import Flask, render_template, request, redirect, jsonify
from flask_bootstrap import Bootstrap
import sys
import os
scriptpath = os.path.abspath('./python/')
sys.path.insert(0, scriptpath)
staticpath = os.path.abspath('./static/')
sys.path.insert(0, staticpath)
#import predict as pdict
import urllib

print ("Laalu")

app = Flask(__name__)
bootstrap = Bootstrap(app)

path = ""
ques = ""
nlp = ""
encoder = ""
model = ""
i = 0

@app.route('/', methods = ['GET'])
def initial():
    print ("Hoola")
    global nlp
    global encoder
    global model
    #nlp, encoder, model = pdict.load()
    return render_template("index.html")


@app.route('/image', methods = ['POST', 'GET'])
def image():
    print (request.form['src'])
    url = request.form['src']
    #image_url = "http://127.0.0.1:5000/static/room.jpg"
    
    #global i
    #global path
    path = ('demo_'+str(i+1)+'.jpg')
    #print(path)
    #TODO: Save the image and make a path of it
    urllib.urlretrieve(url, path)
    #print ("saved image")
    return render_template("index.html")
    
@app.route('/ques', methods = ['POST'])
def ques():
    print ("Quesion is called")
    global ques
    ques = request.form['ques']
    print ("question is ", ques)
    return render_template("index.html")

    
@app.route('/answer', methods = ['GET', 'POST'])
def answer():
    answer = "bull" 
    #answer = str(pdict.predict(nlp, encoder, model, path, ques))
    print (answer)
    return jsonify(ans = answer)
    
        
if __name__ == '__main__':
    app.run(debug = True)
    
    
