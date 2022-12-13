import pandas as pd
import tensorflow as tf
from keras.layers import Dense
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
from tensorflow.python.keras import Sequential

'''
Iris Species
Classify iris plants into three species in this classic dataset
'''
class IrisModel(object):
    def __init__(self):
        # self.iris = pd.read_csv(r'C:\Users\bitcamp\PycharmProjects\djangoProject\shop\flower\data\Iris.csv')
        self.iris = datasets.load_iris()
        print(f'tpye {type(self.iris)}')    # tpye <class 'sklearn.utils.Bunch'>
        self._X = self.iris.data
        self._Y = self.iris.target

    def hook(self):
        self.create_model()

    def spec(self):
        print(self.iris)
        print(f'{self.iris.feature_names}')
        '''
        iris = self.iris
        print(" --- 1.Shape ---")
        print(iris.shape)
        print(" --- 2.Features ---")
        print(iris.columns)
        print(" --- 3.Info ---")
        print(iris.info())
        print(" --- 4.Case Top1 ---")
        print(iris.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(iris.tail(3))
        print(" --- 6.Describe ---")
        print(iris.describe())
        print(" --- 7.Describe All ---")
        print(iris.describe(include='all'))
        '''
        '''
        (150, 6)
        ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
        '''

    def create_model(self):
        X = self._X
        Y = self._Y
        enc = OneHotEncoder()
        Y_1hot = enc.fit_transform(Y.reshape(-1,1)).toarray()
        model = Sequential()
        model.add(Dense(4, input_dim=4, activation='relu'))     # 4 : features - 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'
        model.add(Dense(3, activation='softmax'))       # 3 : classes - setosa, versicolor, virginica
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.fit(X,Y_1hot, epochs=300, batch_size=10)
        print('Model Training is completed')

        file_name = './save/iris_model.h5'
        model.save(file_name)
        print(f'Model saved in {file_name}')



MENUS = ["Exit", #0
         "Hook",#1
         "Spec",#2
]
menu = {
    "1" : lambda x: x.hook(),
    "2" : lambda x: x.spec(),
}
if __name__ == '__main__':
    def my_menu(ls):
        for i, j in enumerate(ls):
            print(f"{i}. {j}")
        return input('메뉴선택: ')
    if __name__ == '__main__':
        i = IrisModel()
        while True:
            print("####################################################################################################")
            choice = my_menu(MENUS)
            print("####################################################################################################")
            if choice == '0':
                print("종료")
                break
            else:
                menu[choice](i)