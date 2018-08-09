import sys
import os
from glob import glob
from skimage.external import tifffile as tiff
import numpy as np
import pandas as pd

dir = sys.argv[1]
samples = pd.read_csv(sys.argv[2], sep=';', header=0)
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
    samplename = samples[samples['Well'].str.contains(well)]['Sample'].values[0]
    filename = str(samplename) + '_composite.tif'
    filedir = os.path.join(folder, filename)
    tiff.imsave(filedir, im.astype('uint16'), imagej=True)
