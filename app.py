from flask import Flask,jsonify,request,render_template, make_response
import pandas as pd
import numpy as np
from flask_cors import CORS, cross_origin
import json
import markovify as mk
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize as sent_tok
# Reading a JSON file
with open('model1.json', 'r') as f:
    data = json.load(f)
reconstituted_model = mk.Text.from_json(data)



app = Flask(__name__)
cors = CORS(app)




@app.route("/")
def index():
    return("welcome to love letter generation model")


@app.route('/loveletter', methods = ['POST'])
def lovel():
    result = []
    for i in range(10):
        results = reconstituted_model.make_sentence()
        result.append(results)
    return {"result":result}


if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 8080, debug=True)
    