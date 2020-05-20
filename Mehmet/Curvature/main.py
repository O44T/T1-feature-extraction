# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:04:13 2020
@author: mehmet
"""

import numpy as np 

import node_plotting

t = np.arange(10) # the lenght of the curved lines

mypath=r"C:\Users\mehmet\Desktop\images"

data=np.genfromtxt(r'C:\Users\mehmet\Desktop\dataset_03.txt', delimiter='  ', dtype=float)

b = np.arange(start=20, stop=22, step=1, dtype=int)

filename = r'C:\Users\mehmet\Desktop\CSM\filename'


node_plotting.plot_nodes(mypath,filename,b,data,t, parameters = None)
