from shared import *
from flask import jsonify, request
import qif as qif
import numpy as np

def measurePredVuln(app):
  baseUrl = '/app/measure/pred-vuln/'

  @app.route(baseUrl + 'g-pred', methods=['POST'])
  def gPred():
    P = request.json.get('P')
    type = request.json.get('type')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
    return jsonify({'result': str(qif.measure.pred_vuln.G_pred(P, type))})

  @app.route(baseUrl + 'add-leakage', methods=['POST'])
  def pVAddLeakage():
    P = request.json.get('P')
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.measure.pred_vuln.add_leakage(P, pi, C))})

  @app.route(baseUrl + 'binary-channel', methods=['POST'])
  def pVBinaryChannel():
    P = request.json.get('P')
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.measure.pred_vuln.binary_channel(P, pi, C))})

  @app.route(baseUrl + 'mult-capacity', methods=['POST'])
  def pVMultCapacity():
    P = request.json.get('P')
    method = request.json.get('method')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.measure.pred_vuln.mult_capacity(P, C, method))})

  @app.route(baseUrl + 'mult-leakage', methods=['POST'])
  def pVMultLeakage():
    P = request.json.get('P')
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.measure.pred_vuln.mult_leakage(P, pi, C))})

  @app.route(baseUrl + 'posterior', methods=['POST'])
  def pVPosterior():
    P = request.json.get('P')
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.measure.pred_vuln.posterior(P, pi, C))})

  @app.route(baseUrl + 'prior', methods=['POST'])
  def pVPrior():
    P = request.json.get('P')
    pi = request.json.get('pi')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.pred_vuln.prior(P, pi))})
