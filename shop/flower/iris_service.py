import pandas as pd
import tensorflow as tf
from keras.layers import Dense
from keras.models import load_model
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
from tensorflow.python.keras import Sequential

'''
Iris Species
Classify iris plants into three species in this classic dataset
'''


class IrisService(object):
    def __init__(self):
        model = load_model(r'C:\Users\bitcamp\PycharmProjects\djangoProject\shop\flower\save\iris_model.h5')
        graph = tf.get_default_graph()
        target_names = datasets.load_iris().target_names

    def hook(self):
        self.service_model()

    def service_model(self):
        pass

MENUS = ["Exit",  # 0
         "Hook",  # 1
         ]
menu = {
    "1": lambda x: x.hook(),
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