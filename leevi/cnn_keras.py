import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


# print(tf.python.client.device_lib.list_local_devices())
# sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

from tensorflow.keras import datasets, layers, models
# from tensorflow.keras import backend as K
# K.tensorflow_backend._get_available_gpus()

print("Num GPUs available: ", len(tf.config.experimental.list_physical_devices('GPU')))

# quit()


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

history = model.fit(new_train_images, train_labels, batch_size=500, epochs=10000, validation_data=(new_test_images, test_labels))
