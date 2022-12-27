import os

import numpy as np
import tensorflow as tf
from tensorflow import keras

os.environ['KMP_DUPLICATE_LIB_OK']='True'

class FruitsService():
    history = None
    def __init__(self):
        global savepath, model
        savepath = r'C:\Users\bitcamp\PycharmProjects\djangoProject\dlearn\fruits'
        model = keras.models.load_model(savepath+"/CNNClassifier.h5")
        self.class_names = None
        self.test_ds_no_shuffle = None
    def predict(self):
        predictions = model.predict(self.test_ds_no_shuffle)
        score = tf.nn.softmax(predictions[0])
        print('This image most likely belongs to {} with a {:.2f} percent confidence'
              .format(self.class_names[np.argmax(score)], 100*np.max(score)))

        score = tf.nn.softmax(predictions[-1])
        print('This image most likely belongs to {} with a {:.2f} percent confidence'
              .format(self.class_names[np.argmax(score)], 100*np.max(score)))

if __name__ == '__main__':
    FruitsService().predict()