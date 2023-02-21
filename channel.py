from shared import *
from flask import jsonify, request
import qif as qif

def channel(app):
  baseUrl = '/app/channel/'
  @app.route(baseUrl + 'repeated_independent',
             methods=['POST'])
  def repeatedIndependent():
    C = request.json.get('C')
    n = request.json.get('n')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.channel.compose.repeated_independent(C, n))})

  @app.route(baseUrl + 'parallel',
             methods=['POST'])
  def parallel():
    A = request.json.get('A')
    B = request.json.get('B')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      A = prepareMatrix(A)
      B = prepareMatrix(B)
    return jsonify({'result': str(qif.channel.compose.parallel(A, B))})

  @app.route(baseUrl + 'assert-proper',
             methods=['POST'])
  def assertProper():
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.channel.assert_proper(C))})

  @app.route(baseUrl + 'deterministic',
             methods=['POST'])
  def deterministic():
    return true

  @app.route(baseUrl + 'factorize',
             methods=['POST'])
  def factorize():
    A = request.json.get('A')
    B = request.json.get('B')
    col_stoch = request.json.get('col_stoch')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      A = prepareMatrix(A)
      B = prepareMatrix(B)
    return jsonify({'result': str(qif.channel.factorize(A, B, col_stoch))})

  @app.route(baseUrl + 'left-factorize',
             methods=['POST'])
  def leftFactorize():
    A = request.json.get('A')
    B = request.json.get('B')
    col_stoch = request.json.get('col_stoch')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      A = prepareMatrix(A)
      B = prepareMatrix(B)
    return jsonify({'result': str(qif.channel.left_factorize(A, B, col_stoch))})

  @app.route(baseUrl + 'hyper',
             methods=['POST'])
  def hyper():
    C = request.json.get('C')
    pi = request.json.get('pi')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.channel.hyper(C, pi))})

  @app.route(baseUrl + 'identity',
             methods=['POST'])
  def identity():
    n_rows = request.json.get('n_rows')
    type = request.json.get('type')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
    return jsonify({'result': str(qif.channel.identity(n_rows))})

  @app.route(baseUrl + 'is-proper',
             methods=['POST'])
  def isProper():
    C = request.json.get('C')
    mrd = request.json.get('mrd')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.channel.is_proper(C))})

  @app.route(baseUrl + 'iterative-bayesian-update',
             methods=['POST'])
  def iterativeBayesianUpdate():
    C = request.json.get('C')
    out = request.json.get('out')
    start = request.json.get('out')
    max_diff = request.json.get('max_diff')
    max_iter = request.json.get('max_iter')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      out = prepareRow(out)
      start = prepareRow(start)
    return jsonify({'result': str(qif.channel.iterative_bayesian_update(C, out))})


  @app.route(baseUrl + 'no-interference',
             methods=['POST'])
  def noInterference():
    n_cols = request.json.get('n_cols')
    n_rows = request.json.get('n_rows')
    type = request.json.get('type')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
    return jsonify({'result': str(qif.channel.no_interference(n_rows, n_cols, type))})

  @app.route(baseUrl + 'normalize',
             methods=['POST'])
  def chNormalize():
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.channel.normalize(C))})

  @app.route(baseUrl + 'posterior',
             methods=['POST'])
  def chPosterior():
    C = request.json.get('C')
    pi = request.json.get('pi')
    col = request.json.get('col')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.channel.posterior(C, pi, col))})
  
  @app.route(baseUrl + 'posteriors',
             methods=['POST'])
  def chPosteriors():
    C = request.json.get('C')
    pi = request.json.get('pi')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.channel.posteriors(C, pi))})

  @app.route(baseUrl + 'randu',
             methods=['POST'])
  def chRandu():
    n_cols = request.json.get('n_cols')
    n_rows = request.json.get('n_rows')
    type = request.json.get('type')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
    return jsonify({'result': str(qif.channel.randu(n_rows, n_cols, type))})

  @app.route(baseUrl + 'reduced',
             methods=['POST'])
  def chReduced():
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.channel.reduced(C))})

  @app.route(baseUrl + 'sample',
             methods=['POST'])
  def chSample():
    C = request.json.get('C')
    pi = request.json.get('pi')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.channel.sample(C, pi))})

  @app.route(baseUrl + 'sample-n',
             methods=['POST'])
  def chSampleN():
    C = request.json.get('C')
    pi = request.json.get('pi')
    n_samples = request.json.get('n_samples')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
      pi = prepareRow(pi)
    return jsonify({'result': str(qif.channel.sample(C, pi, n_samples))})


  @app.route(baseUrl + 'sum-col-min',
             methods=['POST'])
  def sumColMin():
    C = request.json.get('C')
    isRatio = request.json.get('isRatio')
    if (isRatio):
      qif.set_default_type(qif.rat)
      C = prepareMatrix(C)
    return jsonify({'result': str(qif.channel.sum_column_min(C))})