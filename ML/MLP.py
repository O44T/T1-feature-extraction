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
    print('Welcome to the Bubble Vertex multilayer perceptron program!')
    filenum = input('Please insert the number of files to be processed (1 for single file, 2 for training and test files): ')
    if int(filenum) == 2:
        filepath1=input('\nGive the name of the training set file: ')
        print('Training file name: ',filepath1)
        filepath2=input('\nGive the name of the test set file: ')
        print('Test file name: ',filepath2)
    elif int(filenum) == 1:
        filepath=input('\nGive the name of the data file: ')
        print('Data file name: ',filepath)
    else:
        print('Invalid number of files!')
        exit()
    
    
    print('\nStep #1: We separate the data into train and test sets.')
    
    if int(filenum) == 1:
        inputs = np.loadtxt(filepath, usecols=(3,4,5,6))
        labels = np.loadtxt(filepath, usecols=(7))
        
        T1_counter=0
        for i in labels:
            if i == 1:
                T1_counter=T1_counter+1
        print('\nNumber of T1-events: ',T1_counter)
        print('\nNumber of labels: ',len(labels))
        print('\n Portion of T1-events in raw data: ',T1_counter/len(labels))
        permission='No'
        permission = input('\nUse all positive data? Type "Yes", "No" or "Yes, limited": ')
        if permission == 'Yes':
            data_bulk = np.loadtxt(filepath, usecols=(3,4,5,6,7))
            positive_data = data_bulk[np.where(data_bulk[:,4]==1)]
            negative_data = data_bulk[np.where(data_bulk[:,4]==0)]
            negative_data = negative_data[1:2280,:]
            data_bulk = np.vstack((positive_data,negative_data))
            
            inputs = data_bulk[:,[0,1,2,3]]
            labels = data_bulk[:,[4]]
            T1_counter = 0
            for i in labels:
                if int(i) == 1:
                    T1_counter=T1_counter+1
            print('\nNumber of T1-events: ',T1_counter)
            print('\nNumber of labels: ',len(labels))
            print('\n Portion of T1-events in pre-processed data: ',T1_counter/len(labels))
            logical_labels = 1-labels
            labels = np.hstack((labels, logical_labels))
        elif permission == 'Yes, limited':
            T1_num = input('How many T1-events do you want to use? Write your answer here: ')
            data_bulk = np.loadtxt(filepath, usecols=(3,4,5,6,7))
            positive_data = data_bulk[np.where(data_bulk[:,4]==1)]
            positive_data = positive_data[1:int(T1_num),:]
            negative_data = data_bulk[np.where(data_bulk[:,4]==0)]
            negative_data = negative_data[1:2280,:]
            data_bulk = np.vstack((positive_data,negative_data))
            
            inputs = data_bulk[:,[0,1,2,3]]
            labels = data_bulk[:,[4]]
            T1_counter = 0
            for i in labels:
                if int(i) == 1:
                    T1_counter=T1_counter+1
            print('\nNumber of T1-events: ',T1_counter)
            print('\nNumber of labels: ',len(labels))
            print('\n Portion of T1-events in pre-processed data: ',T1_counter/len(labels))
            logical_labels = 1-labels
            labels = np.hstack((labels, logical_labels))
            
            
            
        
        print('\nCreating opposing version of label columns..')
        if permission == 'No':
            logical_labels = 1 - labels
            labels = np.vstack((labels, logical_labels)).T
        input_train, input_test, labels_train, labels_test = train_test_split(inputs, labels, test_size=0.25, random_state=42)
        
    else:
        input_train = np.loadtxt(filepath1, usecols=(3,4,5,6))
        labels_train = np.loadtxt(filepath1, usecols=(8))
        input_test = np.loadtxt(filepath2, usecols=(3,4,5,6))
        labels_test = np.loadtxt(filepath2, usecols=(8))
        input_train[input_train == 0] = -1
        input_test[input_test == 0] = -1
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
    clf = MLPClassifier(solver=used_solver, alpha=5e-5, hidden_layer_sizes=(5, 1), random_state=1, shuffle=True)
    clf.fit(input_train, labels_train)
    print('Fitting of training data complete.')
    print('Predicting based on test data.')
    print("Training set score: %f" % clf.score(input_train, labels_train))
    print("Test set score: %f" % clf.score(input_test, labels_test))
    
    
    
    
    
    
    
main()