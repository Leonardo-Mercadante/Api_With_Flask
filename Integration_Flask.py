import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random as r

app = Flask(__name__)
run_with_ngrok(app)

d = {
    "name": "Nikola",
    "surname": "Tesla",
    "idade": 60
}

@app.route("/")
def home():
    return "<marquee><h3>http://751a-35-231-173-245.ngrok.io/output</h3></marquee>"

@app.route("/input")
def input_data():
    return jsonify(d)

@app.route('/output', methods=['GET', 'POST'])
def predJson():
    pred = r.choice(["positive", "negative"])
    nd = d.copy()  # Faz uma cópia de d para evitar modificar o dicionário original
    nd["prediction"] = pred
    return jsonify(nd)

if __name__ == "__main__":
    app.run()