from flask import Flask, jsonify, request
from flask_cors import CORS
from fractions import Fraction as rat
import numpy as np
import qif as qif

from measureBayesVuln import measureBayesVuln
from measureGuessing import measureGuessing
from refinement import refinement

app = Flask(__name__)
cors = CORS(app, resources={r"/app/*": {"origins": "*"}})

measureBayesVuln(app)
measureGuessing(app)
refinement(app)


@app.route('/')
def main():
  return ("Hello World")


app.run(host='0.0.0.0')