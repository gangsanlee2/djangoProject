import os.path

import tensorflow as tf
from matplotlib import pyplot as plt
import cv2 as cv

from admin.path import dir_path


class NumberModel(object):

    def __init__(self):
        global mnist, x_train, y_train, x_test, y_test
        # 1. MNIST 데이터셋 임포트
        mnist = tf.keras.datasets.mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        # 2. 데이터 전처리
        x_train, x_test = x_train / 255.0, x_test / 255.0

    def create_model(self):
        # 3. 모델 구성
        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(512, activation=tf.nn.relu),
            tf.keras.layers.Dense(10, activation=tf.nn.softmax)
        ])

        # 4. 모델 컴파일
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        # 5. 모델 훈련
        model.fit(x_train, y_train, epochs=5)

        # 6. 정확도 평가
        test_loss, test_acc = model.evaluate(x_test, y_test)
        print(f'테스트 정확도:{test_acc}')
        model.save(os.path.join(dir_path('mnist_number'), 'save', 'number_model.h5'))

    def show_dataset(self):
        print(f'x_test len is : {len(x_test)}')
        fig, axs = plt.subplots(1, 10, figsize=(10, 10))
        for i in range(10):
            axs[i].imshow(x_test[i], cmap='gray_r')
            axs[i].axis('off')
        fn = "{}.png".format("number")
        plt.savefig(fn)
        target = cv.imread(fn)
        target = cv.resize(target, (1000, 500))
        dir = os.path.join(dir_path('mnist_number'), 'save', 'number_model.h5', 'number.png')
        #cv.imwrite(dir, target)
        plt.show()

MENUS = ["Exit", #0
         "create_model",#1
         "show_dataset",#2
]
menu = {
    "1" : lambda x: x.create_model(),
    "2" : lambda x: x.show_dataset(),
}
if __name__ == '__main__':
    def my_menu(ls):
        for i, j in enumerate(ls):
            print(f"{i}. {j}")
        return input('메뉴선택: ')
    if __name__ == '__main__':
        model = NumberModel()
        while True:
            print("####################################################################################################")
            choice = my_menu(MENUS)
            print("####################################################################################################")
            if choice == '0':
                print("종료")
                break
            else:
                menu[choice](model)