#! /usr/bin/python

# module imports
import math
import matplotlib.pyplot as plt
import numpy as np
import h5py

# begin module classes

################################################################################
# CLASS RESULT 
################################################################################

class result: 

  power_ref = 0.0

  def __init__(self,filename,factor):

    # open hdf5 file
    f = h5py.File(filename,'r')

    # read in keff
    self.keff = f['keff'].value[0]

    # read in power
    self.power = f['power'].value
#   self.power = self.power/np.sum(self.power)*np.sum(self.power > 1.e-11)

    # grid factor
    self.factor = factor

#-------------------------------------------------------------------------------

  def process_norm(self):

    self.power_norm = np.sqrt(np.sum(np.power((self.power_ref - self.power),2)))

################################################################################

def gnuplot_file(results):

  datastr = ""
  for item in results:
    datastr += "{factor} {keff} {norm}\n".format(factor=1.0/item.factor,       \
                                          keff=item.keff,norm=item.power_norm)

  datastr += "e\n"
  for item in results:
    datastr += "{factor} {keff} {norm}\n".format(factor=1.0/item.factor,       \
                                          keff=item.keff,norm=item.power_norm)

  datastr += "e\n"

  outstr = """
set terminal wxt persist
set key horizontal
set key bmargin center
set log x
set ytics nomirror
set y2tics
set log y2
plot '-' using 1:2 with linespoint axes x1y1 title "k-effective", '-' using 1:3 with linespoint axes x1y2 title "L2 norm of nodal power"
  """

  outstr += datastr

  with open("gnuplot.dat",'w') as f:
    f.write(outstr)

#-------------------------------------------------------------------------------

def process_all():

  # write filenames manually to process
  results = []
  temp = result('./mesh10/output.h5',10.0)
  results.append(temp)
  temp = result('./mesh5/output.h5',5.0)
  results.append(temp)
  temp = result('./mesh1/output.h5',1.0)
  results.append(temp)
  temp = result('./mesh05/output.h5',0.5)
  results.append(temp)
  temp = result('./mesh02/output.h5',0.2)
  results.append(temp)
  temp = result('./mesh013/output.h5',0.133333333333333333)
  results.append(temp)
  temp = result('./mesh011/output.h5',0.111111111111111111)
  results.append(temp)
# temp = result('./mesh01/output.h5',0.1)
# results.append(temp)

  # set reference
  result.power_ref = results[len(results)-1].power

  # compute norms of power
  for item in results:
    item.process_norm() 

  # compute norms between meshes
  i = 0
  results[0].power
  while i < len(results)-1:
    norm = np.sqrt(np.sum(np.power((results[i+1].power - results[i].power),2))) 
    i += 1
    print  norm 

  # generate gnuplot file
  gnuplot_file(results)

  return results

################################################################################

if __name__ == "__main__":

  r = process_all() 