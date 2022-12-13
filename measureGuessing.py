from shared import *
from flask import jsonify, request
import qif as qif

def measureGuessing(app):
  @app.route('/app/measure/guessing/add-leakage', methods=['POST'])
  def measure_guessing_addLeakage():
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.guessing.add_leakage(pi, C))})

  @app.route('/app/measure/guessing/mult-leakage', methods=['POST'])
  def measure_guessing_multLeakage():
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.guessing.mult_leakage(pi, C))})

  @app.route('/app/measure/guessing/posterior', methods=['POST'])
  def measure_guessing_posterior():
    pi = request.json.get('pi')
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.guessing.posterior(pi, C))})

  @app.route('/app/measure/guessing/prior', methods=['POST'])
  def measure_guessing_prior():
    pi = request.json.get('pi')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.measure.guessing.prior(pi))})
