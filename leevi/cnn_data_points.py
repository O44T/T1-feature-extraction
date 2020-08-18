import numpy as np

def extract_data(data):

    cnn_data_points = data[:,0:3]
    labels = np.zeros((data.shape[0],2))
    labels[:,0] = data[:,-1]
    labels[:,1] = 1 - data[:,-1]
    return cnn_data_points, labels


input_folder = "../data/dataset_04/"

train_file = input_folder + "dataset_04_2.txt"
test_file = input_folder + "dataset_04_3.txt"


train_data = np.loadtxt(train_file)
test_data = np.loadtxt(test_file)


positive_train_data = train_data[np.where(train_data[:,-1] == 1.)]
negative_train_data = train_data[np.where(train_data[:,-1] == 0.)]
negative_train_data = negative_train_data[:3532,:]

train_data = np.zeros((positive_train_data.shape[0] + negative_train_data.shape[0], positive_train_data.shape[1]))
train_data[:positive_train_data.shape[0],:] = positive_train_data
train_data[positive_train_data.shape[0]:,:] = negative_train_data

print train_data
print positive_train_data.shape, negative_train_data.shape

positive_test_data = test_data[np.where(test_data[:,-1] == 1.)]
negative_test_data = test_data[np.where(test_data[:,-1] == 0.)]
negative_test_data = negative_test_data[:2184,:]

test_data = np.zeros((positive_test_data.shape[0] + negative_test_data.shape[0], positive_test_data.shape[1]))
test_data[:positive_test_data.shape[0],:] = positive_test_data
test_data[positive_test_data.shape[0]:,:] = negative_test_data

print test_data
print positive_test_data.shape, negative_test_data.shape

cnn_data_points, labes = extract_data(train_data)
np.savetxt("train_data_points.txt", cnn_data_points)
np.savetxt("train_labes.txt", labes)

cnn_data_points, labes = extract_data(test_data)
np.savetxt("test_data_points.txt", cnn_data_points)
np.savetxt("test_labes.txt", labes)
