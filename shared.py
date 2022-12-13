from fractions import Fraction as rat
import numpy as np

def getRatio(val):
  if (len(val) == 2):
    return rat(val[0],val[1])
  else:
    return rat(val[0])

def prepareRow(row):
  _row = np.array([], ndmin=2)
  for idr, val in enumerate(row):
    if (idr == 0):
      _row = np.array(getRatio(val), ndmin=1)
    else:
      _row = np.append(_row, [getRatio(val)], axis=0)
  return _row
  
def prepareMatrix(C):
  _C = np.array([], ndmin=2)
  for idc, row in enumerate(C):
    _row = prepareRow(row)
    if (idc == 0):
      _C = np.array(_row, ndmin=2)
    else:
      _C = np.append(_C, [_row], axis=0)
  return _C