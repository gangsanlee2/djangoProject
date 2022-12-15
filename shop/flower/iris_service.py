import numpy as np
import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from keras.saving.save import load_model
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
import os

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
        features = np.reshape(features, (1,4)) # 리스트를 행렬로 변환
        Y_prob = model.predict(features)
        print(f'Y_prob type : {type(Y_prob)}')
        #Y_prob의 타입 : ndarray : n차원의 배열
        predicted = Y_prob.argmax(axis=-1) # 가장 낮은 차원으로 변환
        print(f'predicted type : {type(predicted)}')
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