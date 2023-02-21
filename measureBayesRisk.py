from shared import *
from flask import jsonify, request
import qif as qif

def measureBayesRisk(app):

  @app.route('/app/measure/bayes-risk/add-leakage',
             methods=['POST'])
  def measure_bayesRisk_addLeakage():
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.bayes_risk.add_leakage(pi, C))})

  @app.route('/app/measure/bayes-risk/mult-capacity', methods=['POST'])
  def measure_bayesRisk_multCapacity():
    C = request.json.get('C')
    method = request.json.get('method')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.measure.bayes_risk.mult_capacity(C, method))})

  @app.route('/app/measure/bayes-risk/mult-leakage', methods=['POST'])
  def measure_bayesRisk_multLeakage():
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.bayes_risk.mult_leakage(pi, C))})

  @app.route('/app/measure/bayes-risk/posterior', methods=['POST'])
  def measure_bayesRisk_posterior():
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.bayes_risk.posterior(pi, C))})

  @app.route('/app/measure/bayes-risk/prior', methods=['POST'])
  def measure_bayesRisk_prior():
    pi = request.json.get('pi')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.bayes_risk.prior(pi))})

  @app.route('/app/measure/bayes-risk/strategy', methods=['POST'])
  def measure_bayesRisk_strategy():
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.bayes_risk.strategy(pi, C))})
