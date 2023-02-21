from shared import *
from flask import jsonify, request
import qif as qif

def probab(app):
  baseUrl = '/app/probab/'
  @app.route(baseUrl + 'assert-proper',
             methods=['POST'])
  def probabAssertProper():
    pi = request.json.get('pi')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.probab.assert_proper([1]))})

  @app.route(baseUrl + 'from-grid',
             methods=['POST'])
  def fromGrid():
    grid = request.json.get('grid')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      grid = prepareMatrix(grid)
    return jsonify({'result': str(qif.probab.from_grid(grid))})

  @app.route(baseUrl + 'is-proper',
             methods=['POST'])
  def probabIsProper():
    pi = request.json.get('pi')
    mrd = request.json.get('mrd')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.probab.is_proper(pi))})

  @app.route(baseUrl + 'is-uniform',
             methods=['POST'])
  def isUniform():
    pi = request.json.get('pi')
    mrd = request.json.get('mrd')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.probab.is_uniform(pi))})

  @app.route(baseUrl + 'normalize',
             methods=['POST'])
  def normalize():
    pi = request.json.get('pi')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.probab.normalize(pi))})

  @app.route(baseUrl + 'point',
             methods=['POST'])
  def point():
    n_elem = request.json.get('n_elem')
    x = request.json.get('x')
    type = request.json.get('type')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
    return jsonify({'result': str(qif.probab.point(n_elem, x))})

  @app.route(baseUrl + 'randu',
             methods=['POST'])
  def randu():
    n_elem = request.json.get('n_elem')
    type = request.json.get('type')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
    return jsonify({'result': str(qif.probab.randu(n_elem))})

  @app.route(baseUrl + 'sample',
             methods=['POST'])
  def sample():
    pi = request.json.get('pi')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.probab.sample(pi))})

  @app.route(baseUrl + 'sample-n',
             methods=['POST'])
  def sampleN():
    pi = request.json.get('pi')
    n_samples = request.json.get('n_samples')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.probab.sample(pi, n_samples))})

  @app.route(baseUrl + 'to-grid',
             methods=['POST'])
  def toGrid():
    pi = request.json.get('pi')
    width = request.json.get('width')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.probab.to_grid(pi, width))})

  @app.route(baseUrl + 'uniform',
             methods=['POST'])
  def uniform():
    n_elem = request.json.get('n_elem')
    type = request.json.get('type')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
    return jsonify({'result': str(qif.probab.uniform(n_elem))})