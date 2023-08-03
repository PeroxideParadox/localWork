import ssl
ssl._create_default_https_context=ssl._create_unverified_context

import tensorflow as tf
import numpy as np
from tensorflow import keras

import matplotlib.pyplot as pt

#Keras #Code
fashion_mnist=keras.datasets.fashion_mnist

(train_images,train_labels),(test_images,test_labels)=fashion_mnist .load_data()


pt.imshow(train_images[0],cmap="gray",vmin=0,vmax=225)
pt.show()

model=keras.Sequential([
    keras.layers.Flatten(input_shape=(30,30)),
    keras.layers.Dense(units=128,activation=tf.nn.relu),
    keras.layers.Dense(units=10,activation=tf.nn.softmax)

])
 
model.compile(optimizer=tf.optimizer.Adam(),loss='sparse_catogorical_crossentrophy')
model.fit(train_images,train_labels,epochs=5)
test_loss=model.evaluate(test_images,test_labels)

pt.imshow(test_images[1],cmap='grey',vmin=0,vmax=255)
pt.show()

predictions=model.predict(test_images)

print(list(predictions[1].index(max(predictions[1]))))

print(test_labels[1])

print("Task Done")
