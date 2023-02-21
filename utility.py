from shared import *
from flask import jsonify, request
import qif as qif


def utility(app):
  baseUrl = '/app/utility/'

  @app.route(baseUrl + 'expected-distance', methods=['POST'])
  def expectedDistance():
    C = request.json.get('C')
    pi = request.json.get('pi')
    D = request.json.get('D')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      D = prepareMatrix(D)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.utility.expected_distance(D, pi, C))})