# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:29:55 2020
@author: mehmet
"""


import numpy as np
import math
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import numpy
import cv2
import pylab
import cv2 as cv
import matplotlib.lines
import os
 
mypath=r"C:\Users\mehmet\Desktop\Machine Learning\images"

data=np.genfromtxt(r'C:\Users\mehmet\Desktop\Curvature.txt', delimiter=' ', dtype=float)

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

images = numpy.empty(len(onlyfiles), dtype=object)

b = np.arange(start=301, stop=307, step=1, dtype=int)

for n in range(1,len(onlyfiles)+1):
    dpi = 30
    
    images[n-1] = plt.imread( join(mypath,onlyfiles[n-1]))
    
    num_rows, num_cols,RGB = images[n-1].shape
    
    # What size does the figure need to be in inches to fit the image?
    figsize = num_rows / float(dpi), num_cols / float(dpi)
    
    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])
    
    ax.axis('on')
    
    ax.set(xlim=[-0.5, num_rows - 0.5], ylim=[num_cols - 0.5, -0.5], aspect=1)
    for i in range(1,len(data)+1):
        
        if data[i-1,0]== b[n-1,]:
        
            def getCurve(x0,y0,angle,curvature):
                t = np.arange(20)
                x = t
                y = curvature * t*t
            
                x_new = x*math.cos(angle*np.pi/180) - y*math.sin(angle*np.pi/180) + x0
                y_new = x*math.sin (angle*np.pi/180) + y*math.cos (angle*np.pi/180) + y0
            
                plt.plot(x_new, y_new, 'r', linewidth = 6)
                
               
            plt.imshow(images[n-1], getCurve(data[i-1,1],data[i-1,2],data[i-1,3],data[i-1,7]))
            plt.imshow(images[n-1], getCurve(data[i-1,1],data[i-1,2],data[i-1,4],data[i-1,8]))
            plt.imshow(images[n-1], getCurve(data[i-1,1],data[i-1,2],data[i-1,5],data[i-1,9]))
            plt.imshow(images[n-1], getCurve(data[i-1,1],data[i-1,2],data[i-1,6],data[i-1,10]))
            fig.savefig("im000{}".format(b[n-1])+'.jpg', dpi=dpi, transparent=True) 


