import cv2 as cv
import matplotlib.pyplot as plt
from tensorflow import keras


class MyFashion:
    def __init__(self):
        pass

    def exec(self):
        (train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()
        fig, axs = plt.subplots(1, 10, figsize=(10,10))
        for i in range(10):
            axs[i].imshow(train_input[i], cmap='gray_r')
            axs[i].axis('off')
        fn = "{}.png".format("fashion")
        plt.savefig(fn)
        target = cv.imread(fn)
        target = cv.resize(target, (1000, 500))
        dir = r"C:\Users\bitcamp\ReactProject\multiplex\src\images"
        cv.imwrite(dir+r"\fashion.png", target)
        plt.show()

if __name__ == '__main__':
    m = MyFashion()
    m.exec()