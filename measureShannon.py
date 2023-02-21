from shared import *
from flask import jsonify, request
import qif as qif


def measureShannon(app):

  @app.route('/app/measure/shannon/add-capacity', methods=['POST'])
  def measure_shannon_capacity():
    mrd = request.json.get('mrd')
    md = request.json.get('md')
    C = request.json.get('C')
    return jsonify(
      {'result': str(qif.measure.shannon.add_capacity(C, md, mrd))})

  @app.route('/app/measure/shannon/add-leakage', methods=['POST'])
  def measure_shannon_addLeakage():
    pi = request.json.get('pi')
    C = request.json.get('C')
    return jsonify({'result': str(qif.measure.shannon.add_leakage(pi, C))})

  @app.route('/app/measure/shannon/mult-leakage', methods=['POST'])
  def measure_shannon_multLeakage():
    pi = request.json.get('pi')
    C = request.json.get('C')
    return jsonify({'result': str(qif.measure.shannon.mult_leakage(pi, C))})

  @app.route('/app/measure/shannon/posterior', methods=['POST'])
  def measure_shannon_posterior():
    pi = request.json.get('pi')
    C = request.json.get('C')
    return jsonify({'result': str(qif.measure.shannon.posterior(pi, C))})

  @app.route('/app/measure/shannon/prior', methods=['POST'])
  def measure_shannon_prior():
    pi = request.json.get('pi')
    return jsonify({'result': str(qif.measure.shannon.prior(pi))})
