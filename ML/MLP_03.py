'''
Created on 15 May 2020

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
        inputs = np.loadtxt(filepath, usecols=(3,4,5,6,7,8,9,10,11))
        labels = np.loadtxt(filepath, usecols=(12))
        print(inputs[0])  
        T1_counter=0
        for i in labels:
            if i == 1:
                T1_counter=T1_counter+1
        print('\nNumber of T1-events: ',T1_counter)
        print('\nNumber of labels: ',len(labels))
        print('\n Portion of T1-events in raw data: ',T1_counter/len(labels))
        permission = input('\nUse specified data? Type "Yes" or "No" (For now, only Yes works properly)": ') 
        if permission == 'Yes':
            T1_num = input('How many T1-events do you want to use? Write your answer here: ')
            no_T1_num = input('How many non-T1-events do you want to use? Write your answer here: ')
            data_bulk = np.loadtxt(filepath, usecols=(3,4,5,6,7,8,9,10,11,12))
            scaling_permission = input('Do you want to include input scaling (StandardScaler)? Type "yes" or "no": ')
            positive_data = data_bulk[np.where(data_bulk[:,9]==1)]
            pos_index=random.randint(1,int(positive_data.shape[0]+1))
            if pos_index >= int(positive_data.shape[0]-int(T1_num)):
                pos_index=1
            positive_data = positive_data[pos_index:pos_index+int(T1_num),:]
            negative_data = data_bulk[np.where(data_bulk[:,9]==0)]
            neg_index=random.randint(1,int(negative_data.shape[0]+1))
            if neg_index <= int(negative_data.shape[0]-int(no_T1_num)):
                neg_index=1
            negative_data = negative_data[neg_index:neg_index+int(no_T1_num),:]
            
            data_bulk = np.vstack((positive_data,negative_data))
            np.random.shuffle(data_bulk)
            labels = data_bulk[:,[9]]
            if scaling_permission == 'yes':
                print('\nWe scale the separated input data according to StandardScaler.')
                data_bulk = np.delete(data_bulk,9,1)
                data_bulk = StandardScaler().fit_transform(data_bulk)
                data_bulk = np.hstack((data_bulk,labels))
                print('\nScaling training inputs complete.')
            else:
                print('\nInput data is not scaled.')
            inputs = data_bulk[:,[0,1,2,3,4,5,6,7,8]] #Original: 0,1,2,3,4,5,6,7,8
            
            randomize_labels = input('Randomize label column? Write "Yes" or "No": ')
            if randomize_labels == 'Yes':
                np.random.shuffle(labels)
            T1_counter = 0
            for i in labels:
                if int(i) == 1:
                    T1_counter=T1_counter+1
            print('\nNumber of T1-events: ',T1_counter)
            print('\nNumber of labels: ',len(labels))
            print('\n Portion of T1-events in pre-processed data: ',T1_counter/len(labels))
            logical_labels = 1-labels
            labels = np.hstack((labels, logical_labels))
            different_test_set_permission = input("\nCreate another version of test set with different T1-ratio? Type answer here: ")
            if different_test_set_permission == 'Yes':
                T1_num_2 = input('How many T1-events do you want to use? Write your answer here: ')
                no_T1_num_2 = input('How many non-T1-events do you want to use? Write your answer here: ')
                data_bulk_2 = np.loadtxt(filepath, usecols=(3,4,5,6,7,8,9,10,11,12))
        
                positive_data_2 = data_bulk[np.where(data_bulk[:,9]==1)]
                pos_index_2=random.randint(1,int(positive_data_2.shape[0]+1))
                if pos_index_2 >= int(positive_data_2.shape[0]-int(T1_num)):
                    pos_index_2=1
                    positive_data_2 = positive_data[pos_index_2:pos_index_2+int(T1_num_2),:]
                negative_data_2 = data_bulk_2[np.where(data_bulk_2[:,9]==0)]
                neg_index_2=random.randint(1,int(negative_data_2.shape[0]+1))
                if neg_index_2 <= int(negative_data_2.shape[0]-int(no_T1_num_2)):
                    neg_index_2=1
                negative_data_2 = negative_data_2[neg_index_2:neg_index_2+int(no_T1_num_2),:]
                data_bulk_2 = np.vstack((positive_data_2,negative_data_2))
                np.random.shuffle(data_bulk_2)
                labels_2 = data_bulk_2[:,[9]]
                scaling_permission = input('Do you want to include input scaling? Type "yes" or "no": ')
                if scaling_permission == 'yes':
                    print('\nWe scale the separated input data according to StandardScaler.')
                    data_bulk_2 = np.delete(data_bulk_2,9,1)
                    data_bulk_2 = StandardScaler().fit_transform(data_bulk_2)
                    data_bulk_2 = np.hstack((data_bulk_2,labels_2))
                    print('\nScaling training inputs complete.')
                else:
                    print('\nInput data is not scaled.')
                randomize_labels = input('Randomize label column? Write "Yes" or "No": ')
                if randomize_labels == 'Yes':
                    np.random.shuffle(labels_2)
                T1_counter = 0
                for i in labels_2:
                    if int(i) == 1:
                        T1_counter=T1_counter+1
                print('\nNumber of T1-events: ',T1_counter)
                print('\nNumber of labels: ',len(labels_2))
                print('\n Portion of T1-events in pre-processed data: ',T1_counter/len(labels_2))
                inputs_2 = data_bulk_2[:,[0,1,2,3,4,5,6,7,8]] #Original: 0,1,2,3,4,5,6,7,8
                
                logical_labels_2 = 1-labels_2
                labels_2 = np.hstack((labels_2, logical_labels_2))
        print('\nCreating opposing version of label columns..')
        if permission == 'No':
            logical_labels = 1 - labels
            labels = np.vstack((labels, logical_labels)).T
        input_train, input_test, labels_train, labels_test = train_test_split(inputs, labels, test_size=0.20, random_state=0)
        if different_test_set_permission == 'Yes':
            print('\nDiffering TEST set created!')
            input_train_2, input_test, labels_train_2, labels_test = train_test_split(inputs_2, labels_2, test_size=0.20, random_state=0)
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
        T1_counter = 0
        counter = 0
        for i in labels_train:
            if int(i[0]) == 1:
                T1_counter=T1_counter+1
            counter = counter +1
        print('Number of T1-events: ',T1_counter)
        print('Number of cases: ',counter)
    print('Inputs train shape: ',input_train.shape)
    print('Inputs test shape: ',input_test.shape)
    print('Labels train shape: ',labels_train.shape)
    print('Labels test shape: ',labels_test.shape)
    
    print("\nStep #2: Create Multilayer Perceptron, train & predict.")
    print('\nCreating MLP classifier and fitting training data..')
    used_solver = input('Which optimizer algorithms do you wish to use? Type "adam", "sgd" or "lbfgs": ')
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imp = imp.fit(input_train)
    input_train = imp.transform(input_train)
    input_test = imp.transform(input_test)
    clf = MLPClassifier(solver=used_solver, alpha=1e-5, hidden_layer_sizes=(14,20,8,4,), random_state=0, max_iter=20000, shuffle=True)   
    #9,10,11,8,
    #9,18,36,72,144,288,144,72,36,18,9,4,
    #pca = KernelPCA(n_components=2, kernel="poly", degree=1, eigen_solver='arpack', random_state=0)
    pca = PCA(n_components=2, svd_solver='arpack', random_state=0)
    principalComponents = pca.fit_transform(input_train)
    finalDf =  np.hstack((principalComponents, labels_train))
    print("\n------------------------------------------------------------")
    print("\nNumber of features in the original data: ",pca.n_features_)
    print(pd.DataFrame(pca.components_.transpose(),index=['angle1','angle2','angle3','angle4','curvature1','curvature2','curvature3','curvature4','orientation'],columns = ['PC-1','PC-2']))
    print("Data variance ratio after PCA tranform: ",pca.explained_variance_ratio_)
    print("\n------------------------------------------------------------")
    vis_pca = input('\nVisualize PCA components? Type "Yes" or "No": ')
    if vis_pca == "Yes":
        fig = plt.figure(figsize = (8,8))
        ax = fig.add_subplot(1,1,1) 
        ax.set_xlabel('Principal Component 1', fontsize = 15)
        ax.set_ylabel('Principal Component 2', fontsize = 15)
        ax.set_title('PCA: 2 component projection', fontsize = 20)
        targets = [0, 1]
        colors = ['orangered', 'dodgerblue']
        for target, color in zip(targets,colors):
            finalDf_2 = finalDf[np.where(finalDf[:,2] == target)]
            if color == 'r':
                alfa = 0.50
                normi = 1.0
            else:
                alfa = 0.50
                normi=1.0
            ax.scatter(finalDf_2[:,0], finalDf_2[:,1], c = color, alpha=alfa, marker='o', s=5.0, norm=normi)
        ax.legend(targets)
        ax.grid()
        plt.show()
    fit_pca = input('Fit data to PCA? Type "Yes" or "No": ')
    if fit_pca == "Yes":
        input_train = pca.transform(input_train)
        input_test = pca.transform(input_test)
    for i in range(1):
        clf.fit(input_train, labels_train[:,0].reshape(-1,1).ravel())
        predicted = clf.predict(input_test)
        conf_matrix = metrics.confusion_matrix(labels_test[:,0].reshape(-1,1),predicted)
        tn, fp, fn, tp = metrics.confusion_matrix(labels_test[:,0].reshape(-1,1), predicted).ravel()
        print("\n------------------------------------------------------------")
        print('Fitting of training data complete.')
        print('Predicting based on test data.')
        print("\nTraining set score: %f" % clf.score(input_train, labels_train[:,0].reshape(-1,1)))
        print("Test set score: %f" % clf.score(input_test, labels_test[:,0].reshape(-1,1)))
        print('Precision score: ',precision_score(labels_test[:,0].reshape(-1,1), predicted, average='micro'))
        print('Recall score: ',recall_score(labels_test[:,0].reshape(-1,1), predicted, average='micro'))
        print('Confusion matrix: \n')
        print('TN:', tn)
        print('TP: ',tp)
        print('FN: ',fn)
        print('FP:' ,fp)
        print("\n------------------------------------------------------------")
main()