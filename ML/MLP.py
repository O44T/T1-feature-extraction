'''
Created on 22 Apr 2020

@author: oskar
'''
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml
import matplotlib as plt
from matplotlib import pyplot

import numpy as np

def main():
    filepath1 = 'training_set_01.txt'
    filepath2 = 'test_set_01.txt'
    
    print('Training file: ',filepath1)
    print('Testing file: ',filepath2)
    print('\nStep #1: We separate the data into train and test sets.')
    input_train = np.loadtxt(filepath1, usecols=(1,2,3,4,5,6,7))
    labels_train = np.loadtxt(filepath1, usecols=(8))
    input_test = np.loadtxt(filepath2, usecols=(1,2,3,4,5,6,7))
    labels_test = np.loadtxt(filepath2, usecols=(8))
    print('\nCreating opposing version of label columns..')
    logical_train = 1 - labels_train
    logical_test = 1 - labels_test
    labels_train = np.vstack((labels_train, logical_train)).T
    labels_test = np.vstack((labels_test, logical_test)).T
    print('Inputs train shape: ',input_train.shape)
    print('Inputs test shape: ',input_test.shape)
    print('Labels train shape: ',labels_train.shape)
    print('Labels test shape: ',labels_test.shape)
    scaling_permission = input('Do you want to include input scaling? Type "yes" or "no": ')
    if scaling_permission == 'yes':
        print('\nWe scale the separated input data according to StandardScaler.')
        scaler1 = StandardScaler()
        scaler1.fit(input_train) 
        input_train = scaler1.transform(input_train)
        print('\nScaling training inputs complete.')
        scaler2 = StandardScaler()
        scaler2.fit(input_test)  
        input_test = scaler2.transform(input_test)
    else:
        print('\nInput data is not scaled.')
    print("\nStep #2: Create Multilayer Perceptron, train & predict.")
    print('\nCreating MLP classifier and fitting training data..')
    used_solver = input('Which optimizer algorithms do you wish to use? Type "adam", "sgd" or "lbfgs": ')
    clf = MLPClassifier(solver=used_solver, alpha=5e-5, hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(input_train, labels_train)
    print('Fitting of training data complete.')
    print('Predicting based on test data.')
    print("Training set score: %f" % clf.score(input_train, labels_train))
    print("Test set score: %f" % clf.score(input_test, labels_test))
    
    
    
    
    
    
    
main()