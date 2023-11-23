from flask import Flask
from flask_cors import CORS
import math as mt
import flask as jsonify

app = Flask(__name__)
CORS(app)


##SUMA
@app.route("/")
@app.route("/<float:n1>/<float:n2>")
@app.route("/<int:n1>/<int:n2>")
@app.route("/<int:n1>/<float:n2>")
@app.route("/<float:n1>/<int:n2>")
def suma(n1=0,n2=0):
    resultado=n1+n2
    ##return f"<h1> El resultado es: {resultado}</h1><hr>"
    data = {
        "resultado": resultado,
        "operacion": "suma",
    }
    return jsonify(data)

##RESTA
@app.route("/")
@app.route("/resta/<float:n1>/<float:n2>")
@app.route("/resta/<int:n1>/<int:n2>")
@app.route("/resta/<int:n1>/<float:n2>")
@app.route("/resta/<float:n1>/<int:n2>")
def resta(n1=0,n2=0):
    resultado=n1-n2
    ##return f"<h1> El resultado es: {resultado}</h1><hr>"
    data = {
        "resultado": resultado,
        "operacion": "resta",
    }
    return jsonify(data)

##MULTIPLICACION
@app.route("/")
@app.route("/multiplicacion/<float:n1>/<float:n2>")
@app.route("/multiplicacion/<int:n1>/<int:n2>")
@app.route("/multiplicacion/<int:n1>/<float:n2>")
@app.route("/multiplicacion/<float:n1>/<int:n2>")
def multiplicacion(n1=0,n2=0):
    resultado=n1*n2
    ##return f"<h1> El resultado es: {resultado}</h1><hr>"
    data = {
        "resultado": resultado,
        "operacion": "multiplicacion",
    }
    return jsonify(data)

##DIVISION
@app.route("/")
@app.route("/division/<float:n1>/<float:n2>")
@app.route("/division/<int:n1>/<int:n2>")
@app.route("/division/<int:n1>/<float:n2>")
@app.route("/division/<float:n1>/<int:n2>")
def division(n1=0,n2=0):
    resultado=n1/n2
    ##return f"<h1> El resultado es: {resultado}</h1><hr>"
    data = {
        "resultado": resultado,
        "operacion": "division",
    }
    return jsonify(data)

##POTENCIACION
@app.route("/")
@app.route("/potenciacion/<float:n1>/<float:n2>")
@app.route("/potenciacion/<int:n1>/<int:n2>")
@app.route("/potenciacion/<int:n1>/<float:n2>")
@app.route("/potenciacion/<float:n1>/<int:n2>")
def potenciacion(n1=0,n2=0):
    resultado=n1**n2
    ##return f"<h1> El resultado es: {resultado}</h1><hr>"
    data = {
        "resultado": resultado,
        "operacion": "potenciacion",
    }
    return jsonify(data)

##SENO
@app.route("/")
@app.route("/seno/<float:n1>")
@app.route("/seno/<int:n1>")
def seno(n1=0):
    resultado=mt.sin(n1)
    ##return f"<h1> El resultado es: {resultado}</h1><hr>"
    data = {
        "resultado": resultado,
        "operacion": "seno",
    }
    return jsonify(data)

##COSENO
@app.route("/")
@app.route("/coseno/<float:n1>")
@app.route("/coseno/<int:n1>")
def coseno(n1=0):
    resultado=mt.cos(n1)
    ##return f"<h1> El resultado es: {resultado}</h1><hr>"
    data = {
        "resultado": resultado,
        "operacion": "coseno",
    }
    return jsonify(data)

if __name__ == 'main':
    app.run(debug = True)