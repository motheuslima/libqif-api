from shared import *
from flask import jsonify, request
import qif as qif
import numpy as np

def measurePredRisk(app):
  baseUrl = '/app/measure/pred-risk/'

  @app.route(baseUrl + 'l-pred', methods=['POST'])
  def lPred():
    P = request.json.get('P')
    type = request.json.get('type')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
    return jsonify({'result': str(qif.measure.pred_risk.L_pred(P))})

  @app.route(baseUrl + 'add-leakage', methods=['POST'])
  def pRAddLeakage():
    P = request.json.get('P')
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.measure.pred_risk.add_leakage(P, pi, C))})

  @app.route(baseUrl + 'binary-channel', methods=['POST'])
  def pRBinaryChannel():
    P = request.json.get('P')
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.measure.pred_risk.binary_channel(P, pi, C))})

  @app.route(baseUrl + 'mult-capacity', methods=['POST'])
  def prMultCapacity():
    P = request.json.get('P')
    method = request.json.get('method')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.measure.pred_risk.mult_capacity(P, C, method))})

  @app.route(baseUrl + 'mult-leakage', methods=['POST'])
  def pRMultLeakage():
    P = request.json.get('P')
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.measure.pred_risk.mult_leakage(P, pi, C))})

  @app.route(baseUrl + 'posterior', methods=['POST'])
  def pRPosterior():
    P = request.json.get('P')
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.measure.pred_risk.posterior(P, pi, C))})

  @app.route(baseUrl + 'prior', methods=['POST'])
  def pRPrior():
    P = request.json.get('P')
    pi = request.json.get('pi')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.pred_risk.prior(P, pi))})
