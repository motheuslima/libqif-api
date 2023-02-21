from shared import *
from flask import jsonify, request
import qif as qif

def measureGVuln(app):
  baseUrl = '/app/measure/g-vuln/'

  @app.route(baseUrl + 'g-id', methods=['POST'])
  def gId():
    n_rows = request.json.get('n_rows')
    type = request.json.get('type')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
    return jsonify(
      {'result': str(qif.measure.g_vuln.G_id(n_rows, type))})

  @app.route(baseUrl + 'add-capacity', methods=['POST'])
  def gAddCapacity():
    pi = request.json.get('pi')
    C = request.json.get('C')
    one_spanning_g = request.json.get('one_spanning_g')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
    return jsonify(
      {'result': str(qif.measure.g_vuln.add_capacity(pi, C, one_spanning_g))})

  @app.route(baseUrl + 'add-leakage', methods=['POST'])
  def gAddLeakage():
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
      {'result': str(qif.measure.g_vuln.add_leakage(G, pi, C))})

  @app.route(baseUrl + 'g-add', methods=['POST'])
  def gAdd():
    G1 = request.json.get('G1')
    G2 = request.json.get('G2')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      G1 = prepareMatrix(G1)
      G2 = prepareMatrix(G2)
    return jsonify(
      {'result': str(qif.measure.g_vuln.g_add(G1, G2))})

  @app.route(baseUrl + 'g-from-posterior', methods=['POST'])
  def gFromPosterior():
    G = request.json.get('G')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      G = prepareMatrix(G)
      C = prepareMatrix(C)
    return jsonify(
      {'result': str(qif.measure.g_vuln.g_from_posterior(G,C))})

  @app.route(baseUrl + 'g-to-bayes', methods=['POST'])
  def gToBayes():
    pi = request.json.get('pi')
    G = request.json.get('G')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      G = prepareMatrix(G)
    return jsonify(
      {'result': str(qif.measure.g_vuln.g_to_bayes(G, pi))})

  @app.route(baseUrl + 'mult-leakage', methods=['POST'])
  def gMultLeakage():
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
      {'result': str(qif.measure.g_vuln.mult_leakage(G, pi, C))})

  @app.route(baseUrl + 'posterior', methods=['POST'])
  def gPosterior():
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
      {'result': str(qif.measure.g_vuln.posterior(G, pi, C))})

  @app.route(baseUrl + 'prior', methods=['POST'])
  def gPrior():
    pi = request.json.get('pi')
    G = request.json.get('G')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      G = prepareMatrix(G)
    return jsonify(
      {'result': str(qif.measure.g_vuln.prior(G, pi))})

  @app.route(baseUrl + 'strategy', methods=['POST'])
  def gStrategy():
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
      {'result': str(qif.measure.g_vuln.strategy(G, pi, C))})
