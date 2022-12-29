import os
import sys

import numpy as np
from keras.saving.save import load_model
from matplotlib import pyplot as plt
from tensorflow import keras

from admin.path import dir_path


class NumberService(object):
    def __init__(self):
        global model, x_test, y_test
        model = load_model(os.path.join(dir_path('mnist_number'), 'save', 'number_model.h5'))
        (x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()


    def service_model(self, i):
        predictions = model.predict(x_test)
        predictions_array, true_label, img = predictions[i], y_test[i], x_test[i]
        result = np.argmax(predictions_array)
        return result

    def show_number(self, i):
        plt.imshow(x_test[i], cmap='Greys')
        plt.show()

        for x in x_test[i]:
            for n in x:
                sys.stdout.write('%d  ' % n)
            sys.stdout.write('\n')


MENUS = ["Exit",  # 0
         "service_model",  # 1
         "show_number",  # 1
         ]
menu = {
    "1": lambda x: x.service_model(),
    "2": lambda x: x.show_number(),
}
if __name__ == '__main__':
    def my_menu(ls):
        for i, j in enumerate(ls):
            print(f"{i}. {j}")
        return input('메뉴선택: ')


    if __name__ == '__main__':
        service = NumberService()
        while True:
            print(
                "####################################################################################################")
            choice = my_menu(MENUS)
            print(
                "####################################################################################################")
            if choice == '0':
                print("종료")
                break
            else:
                menu[choice](service)