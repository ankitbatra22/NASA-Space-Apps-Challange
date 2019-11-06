from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import random as rng
import matplotlib.pyplot as plt
import astropy
from astropy.io import fits
import os
import matplotlib.pyplot as plt
import matplotlib as pt
import cv2
import numpy as np
import scipy


#def thresh_callback(val):
#   threshold = val
#    canny_output = cv.Canny(src_gray, threshold, threshold * 2)
 #   z = canny_output
 #   print(z)
 #   return z

data = fits.getdata('NEOS_SCI_2019002002143_clean.fits', ext=0)
data = fits.getdata('NEOS_SCI_2019002002349_clean.fits', ext=0)



cv2.imwrite("TEST1.png", data)
cv2.imwrite("TEST2.png", data)





