import os
from shutil import copyfile
import cv2
import numpy as np
from sklearn.preprocessing import LabelBinarizer
from matplotlib import pyplot as plt
from random import seed
from random import randint
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from tensorflow.keras.layers import BatchNormalization
from keras.layers.core import Dropout
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras.optimizers import SGD
from tensorflow.keras.utils import img_to_array
import h5py
from tensorflow.keras.models import model_from_json


class Model:
    def __init__(self):
        pass

    def predict(self, imagePath):
        age_range = [1, 11, 21, 32, 43, 54, 65, 71, 82, 90, 102]
        loaded_model = self.getModel()
        img = cv2.imread(imagePath)
        imgNorm = self.getNormalizedImage(img, 128)
        y_pred = loaded_model.predict(imgNorm)
        return age_range[np.argmax(y_pred[0])]

    def getModel(self):
        json_file = open(r'D:\Project\Project\model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights(r"D:\Project\Project\model1.model")
        loaded_model.compile(loss="categorical_crossentropy", optimizer=SGD(
            learning_rate=0.01), metrics=["accuracy"])
        return loaded_model

    def getNormalizedImage(self, img, imgsize):
        img = cv2.resize(img, (imgsize, imgsize), cv2.INTER_AREA)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = img_to_array(img, data_format='channels_last')
        img = (np.array([img])).astype('float')/255.0
        return img
