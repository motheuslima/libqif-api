from shared import *
from flask import jsonify, request
import qif as qif

def refinement(app):
  @app.route('/app/refinement/add-metric', methods=['POST'])
  def refinement_addMetric():
    pi = request.json.get('pi')
    A = request.json.get('A')
    B = request.json.get('B')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      A = prepareMatrix(A)
      B = prepareMatrix(B)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.refinement.add_metric(pi, A, B))})

  @app.route('/app/refinement/max-refined-by', methods=['POST'])
  def refinement_maxRefinedBy():
    A = request.json.get('A')
    B = request.json.get('B')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      A = prepareMatrix(A)
      B = prepareMatrix(B)
    return jsonify({'result': str(qif.refinement.max_refined_by(A, B))})

  @app.route('/app/refinement/add-metric-bound', methods=['POST'])
  def refinement_addMetricBound():
    A = request.json.get('A')
    B = request.json.get('B')
    pi = request.json.get('pi')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      A = prepareMatrix(A)
      B = prepareMatrix(B)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.refinement.add_metric_bound(pi, A, B))})

  @app.route('/app/refinement/priv-refined-by', methods=['POST'])
  def refinement_privRefinedBy():
    A = request.json.get('A')
    B = request.json.get('B')
    return jsonify({'result': str(qif.refinement.priv_refined_by(A, B))})

  @app.route('/app/refinement/refined-by', methods=['POST'])
  def refinement_refinedBy():
    A = request.json.get('A')
    B = request.json.get('B')
    method = request.json.get('method') or 'factorize'
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      A = prepareMatrix(A)
      B = prepareMatrix(B)
    return jsonify({'result': str(qif.refinement.refined_by(A, B, method))})