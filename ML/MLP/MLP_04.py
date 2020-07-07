'''
Created on 6 Jul 2020

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

import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tsne_visualization
import feature_derivation
import math

def main():
    datafile = input('Filename: ')
    print('\nKeep in mind that bad lines are skipped in original data format.')
    df = pd.read_csv(datafile, sep="   ", error_bad_lines=False)
    print('\nChosen filename: ',datafile)
    df.columns = ['frame_number','T1_x','T1_y','1_mx','1_my','1_ex','1_ey','2_mx','2_my','2_ex','2_ey','3_mx','3_my','3_ex','3_ey','4_mx','4_my','4_ex','4_ey','orientation','label']
    print('--------------------------------------------------------------------------------------')
    print('\nData information section.')
    print('\nDataFrame description:')
    print(df.describe())
    print('\nDataFrame info:')
    print(df.info())
    print('--------------------------------------------------------------------------------------')
    data_manipulation = input('Use data manipulation? Type "Yes" or "No": ')
    if data_manipulation == "Yes":
        manipulation_type = input('\nWhich manipulation type do you want to use? Type answer here: ')
        if manipulation_type == "Angle-S1":
            print('Calculating direct angles between end points.')
            df = feature_derivation.angle(df)
        elif manipulation_type == "Angle-S2":
            print('Calculating direct angles between end points AND substracting them from flow orientation.')
            df = feature_derivation.angle(df)
            df = feature_derivation.orientation_strategy(df)
            
        else:
            print('\nDesired manipulation method has not yet been implemented. Exiting program.')
            exit()
    else:
        print('\nData will not be manipulated in any way.')
        print('--------------------------------------------------------------------------------------')
    strat = input('\nWhich stratagem do we use? 1: [50-50 + 50-50], 2: [50-50 + 10-90], 3: [10-90 + 10-90]: ')
    num_sample = input('\nWhat is the standard sample size? ')
    
    if int(strat) == 1:
        print('\nStratagem 1 chosen.')
        positives = df[df['label']==1]
        positives = positives.sample(n=int((num_sample)*0.5), random_state=1)
        zeros = df[df['label']==0]
        zeros= zeros.sample(n=int(int(num_sample)*0.5), random_state=1)
        frames = [positives, zeros]
        df = pd.concat(frames)
        labels = df['label']
        print(df.columns)
        inputs = df.drop(['frame_number','T1_x','T1_y','label'],1)
        input_train, input_test, labels_train, labels_test = train_test_split(inputs, labels, test_size=0.20, random_state=0)
    elif int(strat) == 2:
        print('\nStratagem 2 chosen.')
        positives = df[df['label']==1]
        positives = positives.sample(n=int(int(num_sample)*0.5), random_state=1)
        zeros = df[df['label']==0]
        zeros= zeros.sample(n=int(num_sample), random_state=1)
        frames = [positives, zeros]
        df = pd.concat(frames)
        labels = df['label']
        
        inputs = df.drop(['frame_number','T1_x','T1_y','label'],1)
        input_train, input_test, labels_train, labels_test = train_test_split(inputs, labels, test_size=0.20, random_state=0)
        positives_2 = positives.sample(n=int(int(num_sample)*0.1), random_state=1)
        zeros_2 = df[df['label']==0]
        zeros_2= zeros_2.sample(n=int(int(num_sample)*0.9), random_state=1, replace=False)
        frames_2 = [positives_2, zeros_2]
        temp_df = pd.concat(frames_2)
        labels_2 = temp_df['label']
        
        inputs_2 = temp_df.drop(['frame_number','T1_x','T1_y','label'],1)
        input_train_2, input_test, labels_train_2, labels_test = train_test_split(inputs_2, labels_2, test_size=0.20, random_state=0)
        
    elif int(strat) == 3:
        print('\nStratagem 3 chosen.')
        positives = df[df['label']==1]
        positives = positives.sample(n=int(int(num_sample)*0.1), random_state=1)
        zeros = df[df['label']==0]
        zeros= zeros.sample(n=int(int(num_sample)*0.9), random_state=1)
        frames = [positives, zeros]
        df = pd.concat(frames)
        labels = df['label']
        
        inputs = df.drop(['frame_number','T1_x','T1_y','label'],1)
        input_train, input_test, labels_train, labels_test = train_test_split(inputs, labels, test_size=0.20, random_state=0)
    else:
        print('\nInvalid stratagem. Exiting program.')
        exit()
    scale_data = input('\nScale the data? Type "Yes" or "No": ')
    if scale_data  == "Yes":
        print('Scaling following features', inputs.columns)
        input_train = StandardScaler().fit_transform(input_train)
        input_test = StandardScaler().fit_transform(input_test)
        
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp = imp.fit(input_train)
    input_train = imp.transform(input_train)
    input_test = imp.transform(input_test)
    solver_type = input('\nWhich ML solver do we use: ')
    clf = MLPClassifier(solver=solver_type, alpha=1e-5, hidden_layer_sizes=(9,10,11,8,), random_state=0, max_iter=20000, shuffle=True)   
    clf.fit(input_train, labels_train)
    predicted = clf.predict(input_test)
    conf_matrix = metrics.confusion_matrix(labels_test,predicted)
    tn, fp, fn, tp = metrics.confusion_matrix(labels_test, predicted).ravel()
    print("\n------------------------------------------------------------")
    print('Fitting of training data complete.')
    print('Predicting based on test data.')
    print("\nTraining set score: %f" % clf.score(input_train, labels_train))
    print("Test set score: %f" % clf.score(input_test, labels_test))
    #print('Precision score: ',precision_score(labels_test, predicted, average='micro'))
    #print('Recall score: ',recall_score(labels_test, predicted, average='micro'))
    print('Confusion matrix: \n')
    print('TN:', tn)
    print('TP: ',tp)
    print('FN: ',fn)
    print('FP:' ,fp)
    print("\n------------------------------------------------------------")
main()
    