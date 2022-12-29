import keras.layers
from keras.datasets import imdb
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from keras_preprocessing.sequence import pad_sequences
from keras import Sequential, utils, optimizers, callbacks

class ImdbModel(object):
    def __init__(self):
        global train_input, train_target, test_input, test_target, val_input, val_target, train_seq, val_seq, train_oh, val_oh
        (train_input, train_target), (test_input, test_target) = imdb.load_data(num_words=500)
        train_input, val_input, train_target, val_target = train_test_split(train_input, train_target, test_size=0.2, random_state=42)
        train_seq = pad_sequences(train_input, maxlen=100) # default : truncating=pre -> post로 바꾸면 앞의 100개만 남김
        val_seq = pad_sequences(val_input, maxlen=100)
        train_oh = utils.to_categorical(train_seq)
        val_oh = utils.to_categorical(val_seq)
        self.model = None

    def preprocess(self):
        print(f'train_input.shape, test_input.shape >>> {train_input.shape}, {test_input.shape}')
        print(f'첫번째 리뷰의 길이 {len(train_input[0])}')
        print(f'두번째 리뷰의 길이 {len(train_input[1])}')
        print(f'첫번째 리뷰의 내용 \n{print(train_input[0])}')
        print(f'타깃 데이터 출력 \n {print(train_target[:20])}') # 1:긍정, 2:부정
        lengths = np.array([len(x) for x in train_input])
        print(f'리뷰 길이의 평균값 : {np.mean(lengths)}\n'
              f'리뷰 길이의 중간값 : {np.median(lengths)}')
        plt.hist(lengths)
        plt.xlabel('length')
        plt.ylabel('frequency')
        plt.show()
        print(f'train_seq.shape is {train_seq.shape}')
        print(f'train_seq 첫번째 샘플 : \n{train_seq[0]}')
        print(f'샘플 원본의 끝 10자리 : {train_input[0][-10:]}')
        print(f'train_seq 여섯번째 샘플 : \n{train_seq[5]}') # truncating=pre 이므로 토큰 패딩도 앞부분에 추가됨

    def create_model(self):
        model = Sequential()
        sample_length = 100
        freq_words = 500
        model.add(keras.layers.SimpleRNN(8, input_shape=(sample_length, freq_words)))
        model.add(keras.layers.Dense(1, activation='sigmoid'))
        print(f'train_oh.shape is {train_oh.shape}')
        print(f'train_oh의 첫번째 샘플의 첫번째 토큰 10 : {print(train_oh[0][0][:12])}')
        print(f'np.sum(train_oh[0][0]) is {np.sum(train_oh[0][0])}')
        model.summary()
        self.model = model

    def fit(self):
        model = self.model
        rmsprop = optimizers.RMSprop(learning_rate=1e-4)
        model.compile(optimizer=rmsprop, loss='binary_crossentropy', metrics=['accuracy'])
        checkpoint_cb = callbacks.ModelCheckpoint('data/best-simplernn-model.h5', save_best_only=True)
        early_stopping_cb = callbacks.EarlyStopping(patience=3, restore_best_weights=True)
        history = model.fit(train_oh, train_target, epochs=100, batch_size=64,
                            validation_data=(val_oh, val_target),
                            callbacks=[checkpoint_cb, early_stopping_cb])
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.legend(['train','val'])
        plt.show()
        print(f'train_seq.nbytes is {train_seq.nbytes}\n '
              f'train_oh.nbytes is {train_oh.nbytes}')

    def hook(self):
        self.create_model()
        self.fit()

class NaverMovieModel(object):
    def __init__(self):
        pass

if __name__ == '__main__':
    ImdbModel().hook()