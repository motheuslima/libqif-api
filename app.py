from flask import Flask, jsonify, request, json
from flask_cors import CORS
from fractions import Fraction as rat
import numpy as np
import qif as qif
import random, string
from werkzeug.exceptions import HTTPException
import traceback

from measureBayesVuln import measureBayesVuln
from measureGuessing import measureGuessing
from measureShannon import measureShannon
from measureLRisk import measureLRisk
from measureGVuln import measureGVuln
from measurePredRisk import measurePredRisk
from measurePredVuln import measurePredVuln
from measureBayesRisk import measureBayesRisk
from refinement import refinement
from channel import channel
from probab import probab
from metric import metric
from utility import utility

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

measureBayesVuln(app)
measureGuessing(app)
measureShannon(app)
measureLRisk(app)
measureGVuln(app)
measurePredRisk(app)
refinement(app)
channel(app)
probab(app)
metric(app)
measurePredVuln(app)
measureBayesRisk(app)
utility(app)


@app.route('/')
def main():
  return ("Hello World")

@app.errorhandler(HTTPException)
def handle_exception(e):
  """Return JSON instead of HTML for HTTP errors."""
  # start with the correct headers and status code from the error
  response = e.get_response()
  # replace the body with JSON
  response.data = json.dumps({
    "code": e.code,
    "name": e.name,
    "description": e.description,
  })
  response.content_type = "application/json"
  return response


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=random.randint(2000, 9000))
