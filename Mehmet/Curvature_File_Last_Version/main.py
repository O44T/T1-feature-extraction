# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:04:13 2020
@author: mehmet
"""

import numpy as np 

import node_plotting



print('You are in main file')

print('\nPlease do not forget to enter the start, stop and step point before running the script')

# path to dataset where  the images are in
mypath=r"C:\Users\mehmet\Desktop\images"

# data file that contains curvatures and angles with T1_event coordinates 
data=np.genfromtxt(r'C:\Users\mehmet\Desktop\dataset\dataset_04_1.txt', delimiter='  ', dtype=float)

#this array is used to specify the range of images
b = np.arange(start=75, stop=76, step=1, dtype=int)

# Unique line is used for removing duplicates in data file in order to compare image and text file smootly
unique = np.unique(data[:,0], axis = 0 ) 

# path to output folder where the  images with red cross go
filename = r'C:\Users\mehmet\Desktop\CSM\filename'


node_plotting.plot_nodes(mypath,filename,b,data,unique, parameters = None)
