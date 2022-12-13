from shared import *
from flask import jsonify, request
import qif as qif

def measureBayesVuln(app):
  @app.route('/app/measure/bayes-vuln/add-leakage', methods=['POST'])
  def measure_bayesvuln_addLeakage():
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.bayes_vuln.add_leakage(pi, C))})

  @app.route('/app/measure/bayes-vuln/min-entropy-leakage', methods=['POST'])
  def measure_bayesvuln_minEntropyLeakage():
    pi = request.json.get('pi')
    C = request.json.get('C')
    return jsonify({'result': str(qif.measure.bayes_vuln.min_entropy_leakage(pi, C))})

  @app.route('/app/measure/bayes-vuln/mult-capacity', methods=['POST'])
  def measure_bayesvuln_multCapacity():
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.measure.bayes_vuln.mult_capacity(C))})

  @app.route('/app/measure/bayes-vuln/mult-leakage', methods=['POST'])
  def measure_bayesvuln_multLeakage():
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.bayes_vuln.mult_leakage(pi, C))})

  @app.route('/app/measure/bayes-vuln/posterior', methods=['POST'])
  def measure_bayesvuln_posterior():
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.bayes_vuln.posterior(pi, C))})

  @app.route('/app/measure/bayes-vuln/prior', methods=['POST'])
  def measure_bayesvuln_prior():
    pi = request.json.get('pi')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.bayes_vuln.prior(pi))})

  @app.route('/app/measure/bayes-vuln/strategy', methods=['POST'])
  def measure_bayesvuln_strategy():
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.bayes_vuln.strategy(pi, C))})