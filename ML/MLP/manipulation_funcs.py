'''
Created on 13 Jul 2020

@author: oskar
'''
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.decomposition import PCA, KernelPCA
from sklearn.model_selection import train_test_split

from sklearn.impute import SimpleImputer
from sklearn import metrics

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc, average_precision_score
from sklearn.datasets import fetch_openml
from sklearn.model_selection import cross_val_score

import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math



def orientation_angles(df):
    not_done = False
    print('\n- Manipulating angles according to orientation. -')
    i = 0
    alfa_done, mid_done, theta_done = False, False, False
    while not_done == False:
        angle_type = input('\nWhich angle do you want to standardize? Type either "alfa", "mid", "theta" or "all": ')
        if angle_type == 'alfa' and alfa_done == False:
            print('Angles 1, 2, 3 and 4 are transformed.')
            df['angle1'] = df['orientation'] - df['angle1']
            df['angle2'] = df['orientation'] - df['angle2']
            df['angle3'] = df['orientation'] - df['angle3']
            df['angle4'] = df['orientation'] - df['angle4']
            alfa_done = True
        elif angle_type == 'mid' and mid_done == False:
            print('Angles 1, 2, 3 and 4 are transformed.')
            df['mid1'] = df['orientation'] - df['mid1']
            df['mid2'] = df['orientation'] - df['mid2']
            df['mid3'] = df['orientation'] - df['mid3']
            df['mid4'] = df['orientation'] - df['mid4']
            mid_done = True
        elif angle_type == 'theta' and theta_done == False:
            print('Angles 1, 2, 3 and 4 are transformed.')
            df['theta1'] = df['orientation'] - df['theta1']
            df['theta2'] = df['orientation'] - df['theta2']
            df['theta3'] = df['orientation'] - df['theta3']
            df['theta4'] = df['orientation'] - df['theta4']
            theta_done = True
        elif angle_type == 'all' and i == 0:
            df['angle1'] = df['orientation'] - df['angle1']
            df['angle2'] = df['orientation'] - df['angle2']
            df['angle3'] = df['orientation'] - df['angle3']
            df['angle4'] = df['orientation'] - df['angle4']
            df['mid1'] = df['orientation'] - df['mid1']
            df['mid2'] = df['orientation'] - df['mid2']
            df['mid3'] = df['orientation'] - df['mid3']
            df['mid4'] = df['orientation'] - df['mid4']
            df['theta1'] = df['orientation'] - df['theta1']
            df['theta2'] = df['orientation'] - df['theta2']
            df['theta3'] = df['orientation'] - df['theta3']
            df['theta4'] = df['orientation'] - df['theta4']
            
            print('All possible angles have been transformed. ')
            return df
        else:
            print('\nAngle type invalid. Alternatively, angle type cannot be transformed more than once.')
        continue_angle_manipulation = input('Continue with the angle manipulation: ')
        if i > 2:
            print('All possible angles have been transformed')
            
            return df
        if continue_angle_manipulation == "No":
            print('Very well, then. Angles will not be modified further.')
            
            return df
        i = i + 1
            