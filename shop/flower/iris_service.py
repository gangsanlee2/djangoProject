import numpy as np
import pandas as pd
import tensorflow as tf
from keras.layers import Dense
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
from tensorflow import keras
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.models import load_model

'''
Iris Species
Classify iris plants into three species in this classic dataset
'''


class IrisService(object):
    def __init__(self):
        global model, graph, target_names
        model = load_model(r'C:\Users\bitcamp\PycharmProjects\djangoProject\shop\flower\save\iris_model.h5')
        target_names = datasets.load_iris().target_names

    def service_model(self, features):
        features = np.reshape(features, (1,4))
        Y_prob = model.predict(features)
        predicted = Y_prob.argmax(axis=-1)
        return predicted[0]


MENUS = ["Exit",  # 0
         "service_model",  # 1
         ]
menu = {
    "1": lambda x: x.service_model(),
}
if __name__ == '__main__':
    def my_menu(ls):
        for i, j in enumerate(ls):
            print(f"{i}. {j}")
        return input('메뉴선택: ')
    if __name__ == '__main__':
        i = IrisService()
        while True:
            print("####################################################################################################")
            choice = my_menu(MENUS)
            print("####################################################################################################")
            if choice == '0':
                print("종료")
                break
            else:
                menu[choice](i)