from flask import Flask,jsonify,request,render_template, make_response
import pandas as pd
import numpy as np
from flask_cors import CORS, cross_origin
import json
import markovify as mk
# Reading a JSON file
with open('./model/model1.json', 'r') as f:
    data = json.load(f)
reconstituted_model = mk.Text.from_json(data)
import random 



app = Flask(__name__)
cors = CORS(app)




@app.route("/")
def index():
    return("welcome to love letter generation model")


@app.route('/lovelettershort', methods = ['POST'])
def lovel():
    result = {"result":[{"results1":reconstituted_model.make_sentence()},
    {"results2": reconstituted_model.make_sentence()},
    {"results3": reconstituted_model.make_sentence()},
    {"results4": reconstituted_model.make_sentence()},
    {"results5": reconstituted_model.make_sentence()},
    {"results6": reconstituted_model.make_sentence()},
    {"results7": reconstituted_model.make_sentence()},
    {"results8": reconstituted_model.make_sentence()},
    {"results9": reconstituted_model.make_sentence()}
    ]
    }
    return result


@app.route('/loveletterlong', methods = ['POST'])
def loves():
    result = []
    for i in range(10):
        results = reconstituted_model.make_sentence()
        result.append(results)
    return {"result":result}


if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 8000, debug=True)
    
