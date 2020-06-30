'''
Created on Thu Apr 23 20:28:00 2020

@author: mehmet

'''
from  matplotlib import pyplot as plt
from os import listdir
from os.path import isfile, join
import numpy
import cv2
import numpy as np
import pylab
import math
import cv2 as cv
import matplotlib.lines


# mypath=r"C:\Users\mehmet\Desktop\Machine Learning\images_test"
# data=np.genfromtxt(r'C:\Users\mehmet\Desktop\Machine Learning\test_set_01.txt', delimiter='  ', dtype=int)
mypath=r"C:\Users\mehmet\Desktop\Sample"
data=np.genfromtxt(r'C:\Users\mehmet\Desktop\MAchine learning lab\T1_locations.txt', delimiter=' ', dtype=int)
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)



for n in range(0, len(onlyfiles)):
    images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
    
   
    
    cv2.line(images[n], (data[n,1],data[n,2]),(data[n,3],data[n,4]), (255), 3) 
    cv2.line(images[n], (data[n,1],data[n,2]),(data[n,5],data[n,6]), (255), 3) 
    cv2.line(images[n], (data[n,1],data[n,2]), (data[n,7],data[n,8]),(255), 3) 
    cv2.line(images[n], (data[n,1],data[n,2]),(data[n,9],data[n,10]), (255), 3)
    
    
    cv2.circle(images[n], (data[n,1],data[n,2]),3,0,-1)
    cv2.circle(images[n], (data[n,3],data[n,4]),3,0,-1)
    cv2.circle(images[n], (data[n,5],data[n,6]),3,0,-1)
    cv2.circle(images[n], (data[n,7],data[n,8]),3,0,-1)
    cv2.circle(images[n], (data[n,9],data[n,10]),3,0,-1) 
    
    # line_1 = matplotlib.lines.Line2D([0,1], [0,4], linewidth=1, linestyle = "-", color="green")
    # line_2 = matplotlib.lines.Line2D([0,4.5], [0,3], linewidth=1, linestyle = "-", color="red")
    # line_1 = matplotlib.lines.Line2D([0,1], [0,4], linewidth=1, linestyle = "-", color="green")
    # line_2 = matplotlib.lines.Line2D([0,4.5], [0,3], linewidth=1, linestyle = "-", color="red")

 
    cv2.imshow("Image number {}".format(n), images[n])     
    
cv2.waitKey(0)# if it is used it i will get 'image not responding' error 
cv2.destroyAllWindows()  