import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_datasets as tfds
from keras import layers
from tensorflow import keras
from keras.callbacks import ModelCheckpoint
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

class FruitsModel():
    def __init__(self):
        global savepath, trainpath, testpath, batch_size, img_height, img_width, BUFFER_SIZE, num_classes, epochs
        savepath = r'C:\Users\bitcamp\PycharmProjects\djangoProject\dlearn\fruits'
        trainpath = r'C:\Users\bitcamp\PycharmProjects\djangoProject\dlearn\fruits\fruits-360-5\Training'
        testpath = r'C:\Users\bitcamp\PycharmProjects\djangoProject\dlearn\fruits\fruits-360-5\Test'
        batch_size = 32
        img_height = 100
        img_width = 100
        self.class_names = None
        BUFFER_SIZE = 10000
        self.train_ds = None
        self.val_ds = None
        self.test_ds = None
        self.test_ds_no_shuffle = None
        num_classes = 5
        epochs = 20
        self.model = None
        self.history = None

    def hook(self):
        self.train_set()
        self.test_set()
        self.shuffle_data()
        self.create_model()
        self.show_model()
        self.predict()

    def show_apple(self):
        img = tf.keras.preprocessing.image.load_img(trainpath+'/Apple Golden 3/0_100.jpg')
        plt.imshow(img)
        plt.axis("off")
        plt.show()

    def train_set(self):
        self.train_ds = keras.preprocessing.image_dataset_from_directory(
            trainpath,
            validation_split=0.3,
            subset="training",
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size
        )
        self.val_ds = keras.preprocessing.image_dataset_from_directory(
            trainpath,
            validation_split=0.3,
            subset="validation",
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size
        )
        self.class_names = self.train_ds.class_names
        print(self.class_names)

    def test_set(self):
        test_ds = keras.preprocessing.image_dataset_from_directory(
            testpath,
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size
        )
        test_ds_no_shuffle = keras.preprocessing.image_dataset_from_directory(
            testpath,
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size,
            shuffle=False
        )
        print(f'type(test_ds) : {type(test_ds)}')
        y = np.concatenate([y for x, y in test_ds], axis=0)
        print(y)
        print('####################################################################################################')
        y = np.concatenate([y for x, y in test_ds_no_shuffle], axis=0)
        print(y)
        print('####################################################################################################')
        x = np.concatenate([x for x, y in test_ds_no_shuffle], axis=0)
        print(x[0])

        plt.figure(figsize=(3,3))
        plt.imshow(x[0].astype("uint8"))
        plt.title(self.class_names[y[0]])
        plt.axis("off")
        plt.show()
        self.test_ds = test_ds
        self.test_ds_no_shuffle = test_ds_no_shuffle

        plt.figure(figsize=(3,3))
        plt.imshow(x[0].astype("uint8"))
        plt.title(self.class_names[y[-1]])
        plt.axis("off")
        plt.show()

    def shuffle_data(self):
        AUTOTUNE = tf.data.experimental.AUTOTUNE
        self.train_ds = self.train_ds.cache().shuffle(BUFFER_SIZE).prefetch(buffer_size=AUTOTUNE)
        self.val_ds = self.val_ds.cache().prefetch(buffer_size=AUTOTUNE)
        self.test_ds = self.test_ds.cache().prefetch(buffer_size=AUTOTUNE)
        print(f'train_ds type : {type(self.train_ds)}')

    def create_model(self):
        model = keras.Sequential([
            keras.layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height,img_width,3)),
            layers.Conv2D(16, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(2),
            layers.Dropout(.50),
            layers.Conv2D(32, 3, padding='same', activation='relu'),
            layers.MaxPooling2D(2),
            layers.Dropout(.50),
            layers.Flatten(),
            layers.Dense(500, activation='relu'),
            layers.Dropout(.50),
            layers.Dense(num_classes, activation='softmax')
            ])
        model.summary()


        model.compile(
            optimizer='adam',
            loss=tf.losses.SparseCategoricalCrossentropy(),
            metrics=['accuracy']
        )

        checkpointer = ModelCheckpoint('CNNClassifier.h5', save_best_only=True)
        early_stopping_cb = keras.callbacks.EarlyStopping(patience=5,
                                                          monitor='val_accuracy',
                                                          restore_best_weights=True)

        self.history = model.fit(
            self.train_ds,
            batch_size=batch_size,
            validation_data=self.val_ds,
            epochs=epochs,
            callbacks=[checkpointer,early_stopping_cb]
        )
        self.model = model

    def show_model(self):
        history = self.history
        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']
        loss = history.history['loss']
        val_loss = history.history['val_loss']
        epochs_range = range(1,len(acc)+1)

        plt.figure(figsize=(10,5))
        plt.subplot(1,2,1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(1,2,2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Loss')
        plt.show()

    def predict(self):
        predictions = self.model.predict(self.test_ds_no_shuffle)
        score = tf.nn.softmax(predictions[0])
        print('This image most likely belongs to {} with a {:.2f} percent confidence'
              .format(self.class_names[np.argmax(score)], 100*np.max(score)))
        score = tf.nn.softmax(predictions[-1])
        print('This image most likely belongs to {} with a {:.2f} percent confidence'
              .format(self.class_names[np.argmax(score)], 100*np.max(score)))

if __name__ == '__main__':
    FruitsModel().hook()