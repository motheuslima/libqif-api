from shared import *
from flask import jsonify, request
import qif as qif

def measureLRisk(app):
  baseUrl = '/app/measure/l-risk/'

  @app.route(baseUrl + 'l-zero-one', methods=['POST'])
  def lZeroOne():
    n_rows = request.json.get('n_rows')
    type = request.json.get('type')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
    return jsonify(
      {'result': str(qif.measure.l_risk.L_zero_one(n_rows, type))})

  @app.route(baseUrl + 'add-capacity', methods=['POST'])
  def lAddCapacity():
    pi = request.json.get('pi')
    C = request.json.get('C')
    one_spanning_g = request.json.get('one_spanning_g')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
    return jsonify(
      {'result': str(qif.measure.l_risk.add_capacity(pi, C, one_spanning_g))})

  @app.route(baseUrl + 'add-leakage', methods=['POST'])
  def lAddLeakage():
    pi = request.json.get('pi')
    C = request.json.get('C')
    G = request.json.get('G')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
      G = prepareMatrix(G)
    return jsonify(
      {'result': str(qif.measure.l_risk.add_leakage(G, pi, C))})

  @app.route(baseUrl + 'mult-leakage', methods=['POST'])
  def lMultLeakage():
    pi = request.json.get('pi')
    C = request.json.get('C')
    G = request.json.get('G')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
      G = prepareMatrix(G)
    return jsonify(
      {'result': str(qif.measure.l_risk.mult_leakage(G, pi, C))})

  @app.route(baseUrl + 'posterior', methods=['POST'])
  def lPosterior():
    pi = request.json.get('pi')
    C = request.json.get('C')
    G = request.json.get('G')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
      G = prepareMatrix(G)
    return jsonify(
      {'result': str(qif.measure.l_risk.posterior(G, pi, C))})

  @app.route(baseUrl + 'prior', methods=['POST'])
  def lPrior():
    pi = request.json.get('pi')
    G = request.json.get('G')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      G = prepareMatrix(G)
    return jsonify(
      {'result': str(qif.measure.l_risk.prior(G, pi))})

  @app.route(baseUrl + 'strategy', methods=['POST'])
  def lStrategy():
    pi = request.json.get('pi')
    C = request.json.get('C')
    G = request.json.get('G')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
      G = prepareMatrix(G)
    return jsonify(
      {'result': str(qif.measure.l_risk.strategy(G, pi, C))})
