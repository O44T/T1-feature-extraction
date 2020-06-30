
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:50:09 2020
@author: mehmet
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2

dpi = 30

img = plt.imread('im000310.jpg')
num_rows, num_cols,RGB = img.shape
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), -40, 0.7)
img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
# cv2.imshow('Rotation',img_rotation)
# cv2.imwrite('img.png',img_rotation)


# What size does the figure need to be in inches to fit the image?
figsize = num_rows / float(dpi), num_cols / float(dpi)

# Create a figure of the right size with one axes that takes up the full figure
fig = plt.figure(figsize=figsize)
ax = fig.add_axes([0, 0, 1, 1])


ax.axis('on')


ax.set(xlim=[-0.5, num_rows - 0.5], ylim=[num_cols - 0.5, -0.5], aspect=1)

def getCurve(x0,y0,curvature):
    t = np.arange(37)
    x = x0+t
    y = y0 + curvature *t*t
    plt.plot(x,y,'r',linewidth = 6)
    
# getCurve(400,205,0.2)
# plt.imshow(cv2.cvtColor(img_rotation,getCurve(382,246,0.01), cv2.COLOR_BGR2RGB))
plt.imshow(img_rotation, getCurve(382,246,0.007))
fig.savefig('curvedImage.jpg', dpi=dpi, transparent=True)
# plt.imshow(img, getCurve(332,252,0.007))

cv2.waitKey(10000)
cv2.destroyAllWindows()