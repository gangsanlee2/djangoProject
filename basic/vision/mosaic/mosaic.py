import copy
import os.path
from io import BytesIO

import numpy as np
from PIL import Image
import requests
import cv2 as cv
from matplotlib import pyplot as plt

from admin.path import dir_path
from basic.pythonic.lambdas import MosaicLambdas
from basic.vision.common import Common


def ImageToNumberArray(url):
    res = requests.get(url, headers={'User-Agent': 'My User Agent 1.0'})
    image = Image.open(BytesIO(res.content))
    return np.array(image)



def GaussianBlur(src, sigmax, sigmay):
    i = np.arange(-4 * sigmax, 4 * sigmax + 1)
    j = np.arange(-4 * sigmay, 4 * sigmay + 1)
    mask = np.exp(-(i ** 2 / (2 * sigmax ** 2))) / (np.sqrt(2 * np.pi) * sigmax)
    maskT = np.exp(-(j ** 2 / (2 * sigmay ** 2))) / (np.sqrt(2 * np.pi) * sigmay)
    mask = mask[:, np.newaxis]
    maskT = maskT[:, np.newaxis].T
    return filter2D(filter2D(src, mask), maskT)

def Canny(src, lowThreshold,highThreshold):
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    Ix = filter2D(src, Kx)
    Iy = filter2D(src, Ky)
    G = np.hypot(Ix, Iy)  # 피타고라스 빗변 구하기
    img = G / G.max() * 255  # 엣지를 그레이스케일로 표현
    D = np.arctan2(Iy, Ix)  # 아크탄젠트 이용해서 그래디언트를 구함

    M, N = img.shape
    Z = np.zeros((M, N), dtype=np.int32)  # 이미지 크기만큼의 행렬을 생성
    angle = D * 180. / np.pi  # 라디안을 degree로 변환(정확하지 않음)
    angle[angle < 0] += 180  # 음수일 때 180을 더함

    for i in range(1, M - 1):
        for j in range(1, N - 1):
            try:
                q = 255
                r = 255

                # angle 0
                if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                    q = img[i, j + 1]
                    r = img[i, j - 1]
                # angle 45
                elif (22.5 <= angle[i, j] < 67.5):
                    q = img[i + 1, j - 1]
                    r = img[i - 1, j + 1]
                # angle 90
                elif (67.5 <= angle[i, j] < 112.5):
                    q = img[i + 1, j]
                    r = img[i - 1, j]
                # angle 135
                elif (112.5 <= angle[i, j] < 157.5):
                    q = img[i - 1, j - 1]
                    r = img[i + 1, j + 1]

                if (img[i, j] >= q) and (img[i, j] >= r):  # 주변 픽셀(q, r)보다 크면 image 행렬의 값을 그대로 사용
                    Z[i, j] = img[i, j]
                else:  # 그렇지 않을 경우 0을 사용
                    Z[i, j] = 0

            except IndexError as e:  # 인덱싱 예외 발생 시 pass
                pass

    M, N = img.shape
    res = np.zeros((M, N), dtype=np.int32)

    weak = np.int32(25)  # 약한 에지
    strong = np.int32(255)  # 강한 에지

    # 이중 임곗값 비교

    # 최대 임곗값보다 큰 원소의 인덱스를 저장
    strong_i, strong_j = np.where(img >= highThreshold)
    # 최소 임곗값보다 작은 원소의 인덱스를 저장
    zeros_i, zeros_j = np.where(img < lowThreshold)

    # 최소 임곗값과 최대 임곗값 사이에 있는 원소의 인덱스를 저장
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))

    # 각각 강한 에지와 약한 에지의 값으로 저장
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak

    for i in range(1, M - 1):
        for j in range(1, N - 1):
            if (img[i, j] == weak):
                try:
                    if ((img[i + 1, j - 1] == strong) or (img[i + 1, j] == strong) or (img[i + 1, j + 1] == strong)
                            or (img[i, j - 1] == strong) or (img[i, j + 1] == strong)
                            or (img[i - 1, j - 1] == strong) or (img[i - 1, j] == strong) or (
                                    img[i - 1, j + 1] == strong)):  # 강한 에지와 연결 되어있을 때
                        img[i, j] = strong  # 연결되어 있는 에지 또한 강한 에지가 됨
                    else:  # 연결되어 있지 않을 때
                        img[i, j] = 0  # 에지가 없는 0으로 설정
                except IndexError as e:
                    pass
    return img

def Hough(edges):
    lines = cv.HoughLinesP(edges, 1, np.pi / 180., 10, minLineLength=50, maxLineGap=5)
    dst = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
    if lines is not None:
        for i in range(lines.shape[0]):
            pt1 = (lines[i][0][0], lines[i][0][1])
            pt2 = (lines[i][0][2], lines[i][0][3])
            cv.line(dst, pt1, pt2, (255, 0, 0), 2, cv.LINE_AA)
    return dst

def Haar(*params):
    haar = cv.CascadeClassifier(os.path.join(dir_path('mosaic'), 'data', params[1]))
    face = haar.detectMultiScale(params[0], minSize=(150, 150))
    if len(face) == 0:
        print("얼굴인식 실패")
        quit()
    for (x, y, w, h) in face:
        print(f'얼굴의 좌표 : {x},{y},{w},{h}')
        red = (255, 0, 0)
        cv.rectangle(params[0], (x, y), (x + w, y + h), red, thickness=20)
        return (x, y, x+w, y+h)

def Mosaic(img, rect, size):
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    i_rect = img[y1:y2, x1:x2]
    i_small = cv.resize(i_rect, (size, size))
    i_mos = cv.resize(i_small, (w, h), interpolation=cv.INTER_AREA)
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2

def Mosaics(img, size):
    haar = cv.CascadeClassifier(os.path.join(dir_path('mosaic'), 'data', 'haarcascade_frontalface_alt.xml'))
    face = haar.detectMultiScale(img, minSize=(150, 150))
    if len(face) == 0:
        print("얼굴인식 실패")
        quit()
    for (x, y, w, h) in face:
        print(f'얼굴의 좌표 : {x},{y},{w},{h}')
        x1 = x
        x2 = x+w
        y1 = y
        y2 = y+h
        i_rect = img[y1:y2, x1:x2]
        i_small = cv.resize(i_rect, (size, size))
        i_mos = cv.resize(i_small, (x2-x1, y2-y1), interpolation=cv.INTER_AREA)
        img[y1:y2, x1:x2] = i_mos
    return img

def filter2D(src, kernel, delta=0):
    halfX = kernel.shape[0] // 2
    halfY = kernel.shape[1] // 2
    cornerPixel = np.zeros((src.shape[0] + halfX * 2, src.shape[1] + halfY * 2), dtype=np.uint8)

    cornerPixel[halfX:cornerPixel.shape[0] - halfX, halfY:cornerPixel.shape[1] - halfY] = src

    dst = np.zeros((src.shape[0], src.shape[1]), dtype=np.float64)

    for y in np.arange(src.shape[1]):
        for x in np.arange(src.shape[0]):
            dst[x, y] = (kernel * cornerPixel[x: x + kernel.shape[0], y: y + kernel.shape[1]]).sum() + delta
    return dst


class MenuController(object):

    @staticmethod
    def menu_0(*params):
         print(params[0])

    @staticmethod
    def menu_1(*params):
        print(params[0])
        img = MosaicLambdas('IMAGE_READ', params[1])
        print(f'cv2 버전 {cv.__version__}')
        print(f' Shape is {img.shape}')
        cv.imshow('Original', img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_2(*params):
        print(params[0])
        arr = ImageToNumberArray(params[1])
        plt.imshow(MosaicLambdas('FROM_ARRAY',arr))
        plt.show()

    @staticmethod
    def menu_3(*params):
        print(params[0])
        img = ImageToNumberArray(params[1])
        print(f'img type : {type(img)}')
        edges = cv.Canny(np.array(img), 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        print(params[0])
        img = ImageToNumberArray(params[1])
        edges = cv.Canny(img, 100, 200)
        lines = cv.HoughLinesP(edges, 1, np.pi / 180., 120, minLineLength=50, maxLineGap=5)
        dst = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
        if lines is not None:
            for i in range(lines.shape[0]):
                pt1 = (lines[i][0][0], lines[i][0][1])
                pt2 = (lines[i][0][2], lines[i][0][3])
                cv.line(dst, pt1, pt2, (255, 0, 0), 2, cv.LINE_AA)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_5(*params):
        print(params[0])
        cat = MosaicLambdas("IMAGE_READ", params[1])
        mos = Mosaic(cat, (200,200,300,300), 10)
        cv.imwrite(os.path.join(dir_path('mosaic'), 'data', 'cat-mosaic.png'), mos)
        cv.imshow("CAT MOSAIC", mos)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_6(*params):
        print(params[0])

        girl = params[2]
        girl = MosaicLambdas("IMAGE_READ", girl)
        girl = cv.cvtColor(girl, cv.COLOR_BGR2RGB)
        girl_for_haar = copy.deepcopy(girl)
        gray = MosaicLambdas('GRAYSCALE',girl)
        edges = cv.Canny(np.array(girl), 100, 200)
        dst = Hough(edges)
        xml = params[1]
        rect = Haar(girl_for_haar, xml)
        girl_mosaic = Mosaic(girl, rect, 10)

        plt.subplot(161), plt.imshow(girl)
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(162), plt.imshow(gray, cmap='gray')
        plt.title('Gray'), plt.xticks([]), plt.yticks([])
        plt.subplot(163), plt.imshow(edges, cmap='gray')
        plt.title('Canny'), plt.xticks([]), plt.yticks([])
        plt.subplot(164), plt.imshow(dst, cmap='gray')
        plt.title('Hough'), plt.xticks([]), plt.yticks([])
        plt.subplot(165), plt.imshow(girl_for_haar)
        plt.title('Haar'), plt.xticks([]), plt.yticks([])
        plt.subplot(166), plt.imshow(girl_mosaic)
        plt.title('Mosaic'), plt.xticks([]), plt.yticks([])

        plt.show()

    @staticmethod
    def menu_7(*params):
        print(params[0])
        with_mom = MosaicLambdas("IMAGE_READ", params[1])
        with_mom = cv.cvtColor(with_mom, cv.COLOR_RGB2BGR)
        with_mom_original = with_mom.copy()
        with_mom_mosaics = Mosaics(with_mom, 10)

        plt.subplot(121), plt.imshow(with_mom_original)
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(with_mom_mosaics)
        plt.title('Mosaics'), plt.xticks([]), plt.yticks([])
        plt.show()

LENNA = "Lenna.png"
SOCCER = "https://docs.opencv.org/4.x/roi.jpg"
BUILDING = "http://amroamroamro.github.io/mexopencv/opencv_contrib/fast_hough_transform_demo_01.png"
HAAR = "haarcascade_frontalface_alt.xml"
GIRL = "girl.jpg"
GIRL_INCLINED = "girl_inclined.png"
GIRL_SIDE_FACE = "girl_side_face.jpg"
GIRL_WITH_MOM = "girl_with_mom.jpg"
CAT = "cat.jpg"

if __name__ == '__main__':
    api = MenuController()
    while True:
        menus = ["종료","원본보기","그레이스케일","엣지검출","직선검출","모자이크","소녀 모자이크","모녀 모자이크"]
        menu = Common.menu(menus)

        if menu == "0":
            api.menu_0(menus[0])
            break
        elif menu == "1": api.menu_1(menus[1],LENNA)
        elif menu == "2": api.menu_2(menus[2],SOCCER)
        elif menu == "3": api.menu_3(menus[3],SOCCER)
        elif menu == "4": api.menu_4(menus[4],BUILDING)
        elif menu == "5": api.menu_5(menus[5],CAT)
        elif menu == "6": api.menu_6(menus[6],HAAR,GIRL)
        elif menu == "7": api.menu_7(menus[7],GIRL_WITH_MOM)
        else:
            print(" ### 해당 메뉴 없음 ### ")