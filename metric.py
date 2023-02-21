from shared import *
from flask import jsonify, request
import qif as qif


def metric(app):
  baseUrl = '/app/metric/'

  @app.route(baseUrl + 'l1-diameter', methods=['POST'])
  def l1Diameter():
    C = request.json.get('C')
    method = request.json.get('method')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.metric.optimize.l1_diameter(C, method))})

  @app.route(baseUrl + 'l2-min-enclosing-ball', methods=['POST'])
  def l2MinEnclosingBall():
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
    return jsonify(
      {'result': str(qif.metric.optimize.l2_min_enclosing_ball(C))})

  @app.route(baseUrl + 'simplex-l1', methods=['POST'])
  def simplexL1():
    C = request.json.get('C')
    method = request.json.get('method')
    in_conv_hull = request.json.get('in_conv_hull')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.metric.optimize.simplex_l1_min_enclosing_ball(C, method, in_conv_hull))})

  @app.route(baseUrl + 'simplex-project', methods=['POST'])
  def simplexProject():
    pi = request.json.get('pi')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.metric.optimize.simplex_project(pi))})

