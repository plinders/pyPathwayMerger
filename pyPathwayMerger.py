import sys
import os
from glob import glob
from skimage.external import tifffile as tiff
import numpy as np

dir = sys.argv[1]

folders = glob(dir+'/*/')

for folder in folders:
    well = folder.split('\\')[-2].split(' ')[1]
    channels = glob(folder+'*.tif')
    channels.sort()
    dim = tiff.imread(channels[0])
    newshape = (3, dim.shape[0], dim.shape[1])
    im = np.zeros(newshape)
    for i, chan in enumerate(channels):
        im[i] = tiff.imread(channels[i])
    filename = str(well) + '_composite.tif'
    filedir = os.path.join(folder, filename)
    tiff.imsave(filedir, im.astype('uint16'))
