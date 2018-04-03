#Convert .mat file to .tif
import numpy as np
import scipy.io as sio
import sys
import tifffile as tif

f=sio.loadmat(sys.argv[1])
data=f['data']

data2=np.moveaxis(data,2,0)
print data2.shape
tif.imsave('%s.tif' %sys.argv[1][:-4], data2.astype(np.int32))
