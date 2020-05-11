# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:29:55 2020

@author: mehmet
"""


import matplotlib.pyplot as plt
import numpy as np
import cv2
import math 

dpi = 30

img = plt.imread('im000310.jpg')
num_rows, num_cols,RGB = img.shape

# What size does the figure need to be in inches to fit the image?
figsize = num_rows / float(dpi), num_cols / float(dpi)

# Create a figure of the right size with one axes that takes up the full figure
fig = plt.figure(figsize=figsize)
ax = fig.add_axes([0, 0, 1, 1])

ax.axis('on')

ax.set(xlim=[-0.5, num_rows - 0.5], ylim=[num_cols - 0.5, -0.5], aspect=1)
def getCurve(x0,y0,curvature, angle):
    t = np.arange(50)
    x = t
    y = curvature * t*t

    x_new = x*math.cos(angle*np.pi/180) - y*math.sin(angle*np.pi/180) + x0
    y_new = x*math.sin (angle*np.pi/180) + y*math.cos (angle*np.pi/180) + y0

    plt.plot(x_new, y_new, 'r', linewidth = 6)
    
   
plt.imshow(img, getCurve(300,201,0.0045,-40))

fig.savefig('curvedImage.jpg', dpi=dpi, transparent=True) 