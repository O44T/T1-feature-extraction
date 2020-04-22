# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:48:29 2020

@author: mehmet
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import cv2
from PIL import Image
import pandas as pd
coordinate = [] 
 
img=cv2.imread(r'C:\Users\mehmet\Desktop\MAchine learning lab\images\im006471.png')

data=np.genfromtxt(r'C:\Users\mehmet\Desktop\MAchine learning lab\T1_locations.txt', delimiter=' ', dtype=int)


for row in data:
    # print('second element = ' + str(row[0]))
    a = row[0]
    
    # print(a)
dst = cv.fastNlMeansDenoisingColored(img,None,7,10,7,21)#  minimizing the noise in image 

coordinate = []
# print(data[0,0])
gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)#  Converting an image from one color space to another. 

gray= np.float32(gray)
   
corners = cv2.goodFeaturesToTrack(gray,1000,0.01,10)# corner tracking module 

corners = np.int0(corners)

# print(range(len(row)))
# k = input('Enter the line number ')
# d = input('Enter the circle number ')

def lines(k):
    for n in range(len(row)) :
        if n==k:
            cv2.line(img, (data[n,1],data[n,2]),(data[n,3],data[n,4]), (255), 3) 
            cv2.line(img, (data[n,1],data[n,2]),(data[n,5],data[n,6]), (255), 3) 
            cv2.line(img, (data[n,1],data[n,2]), (data[n,7],data[n,8]),(255), 3) 
            cv2.line(img, (data[n,1],data[n,2]),(data[n,9],data[n,10]), (255), 3) 
       
        
def circle(k):
    for n in range(len(row)) :
        if n==k:
            cv2.circle(img, (data[n,1],data[n,2]),3,0,-1)
            cv2.circle(img, (data[n,3],data[n,4]),3,0,-1)
            cv2.circle(img, (data[n,5],data[n,6]),3,0,-1)
            cv2.circle(img, (data[n,7],data[n,8]),3,0,-1)
            cv2.circle(img, (data[n,9],data[n,10]),3,0,-1) 
            
# def angle(k):
#     for n in range(len(row)) :
#         if n == k:
#           a =   


for corner in corners :
    x,y = corner.ravel()
    # cv2.circle(img, (x,y),3,(0,100,0),-1)
    # coordinate.append((x,y))
    lines(6)
    circle(6)
    
    
cv2.imshow('img_resize',img)

cv2.waitKey(0)# if it is used it i will get 'image not responding' error 
cv2.destroyAllWindows()



            

    
    
    
    
    
    