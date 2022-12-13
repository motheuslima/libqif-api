from fractions import Fraction as rat
import numpy as np
import qif as qif

def compute_bayes(C):
	pi = qif.probab.uniform(C.shape[0])
  
	print("Channel:\n", C.shape[0])
	print("Prior:\n", pi)

	print("Bayes vulnerability", qif.measure.bayes_vuln.posterior(pi, C))
	print("Bayes mult-capacity", qif.measure.bayes_vuln.mult_capacity(C))

  
def test():
  C = np.array([
  	[0.5, 0.25, 0.25],
  	[0.16666666666, 0.5, 0.33333333333],
  	[0.5, 0.5, 0],
  ])
  
  compute_bayes(C)

  ## qif.set_default_type(qif.rat)
  
  ##  C = np.array([
  ##  	[rat(1,2), rat(1,4), rat(1,4)],
  ##  	[rat(1,6), rat(3,6), rat(2,6)],
  ##  	[rat(1,2), rat(1,2), rat(0)],
  ##  ])
  
  ##  compute_bayes(C)

  ## print(qif.measure.d_privacy.smallest_epsilon(C))
  return jsonify({'result': True})
  