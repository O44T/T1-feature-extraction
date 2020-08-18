import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt


train_images = np.load("train/Xdata.npy") / 255.
train_labels = np.load("train/ydata.npy")
permutation = np.random.permutation(train_labels.shape[0])
train_images = train_images[permutation,:,:,:]
train_labels = train_labels[permutation,0]

new_train_images = np.empty((train_images.shape[0], 100, 100, 1))
new_train_images[:,:,:,0] = train_images[:,0,:,:]


test_images = np.load("test/Xdata.npy") / 255.
test_labels = np.load("test/ydata.npy")
permutation = np.random.permutation(test_labels.shape[0])
test_images = test_images[permutation,:,:,:]
test_labels = test_labels[permutation,0]

new_test_images = np.empty((test_images.shape[0], 100, 100, 1))
new_test_images[:,:,:,0] = test_images[:,0,:,:]


model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(100,100,1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(32, (4, 4), activation="relu"))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(32, (4, 4), activation="relu"))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(10))

model.summary()

model.compile(optimizer="adam", loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=["accuracy"])

history = model.fit(new_train_images, train_labels, epochs=50, validation_data=(new_test_images, test_labels))
