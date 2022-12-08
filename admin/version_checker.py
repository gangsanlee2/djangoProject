import tensorflow as tf
import torch
import sklearn

if __name__ == '__main__':
    print('### tensorflow version ###')
    print(tf.__version__)
    print('### torch version ###')
    print(torch.__version__)
    print('### sklearn version ###')
    print(sklearn.__version__)
    print(' ### CUDA 프로그래밍 가능여부 :  ')
    print(torch.cuda.is_available())