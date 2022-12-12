import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from path import MIDWEST_DATA_CTX, MIDWEST_SAVE_CTX


class Midwest:
    midwest = pd.read_csv(MIDWEST_DATA_CTX+'midwest.csv')
    def menu_1(self):
        print(Midwest.midwest.info())

    def menu_2(self):
        mw = Midwest.midwest
        mw = mw.rename(columns={'poptotal':'total','popasian':'asian'})
        print(mw.info())
        Midwest.midwest = mw

    def menu_3(self):
        mw = Midwest.midwest
        mw['rate_asian'] = (mw['asian'] / mw['total']) * 100
        print(mw)
        Midwest.midwest = mw

    def menu_4(self):
        mw = Midwest.midwest
        avg_rate_asian = sum(mw['rate_asian'])/len(mw['rate_asian'])
        mw['size_popasian'] = np.where(mw['rate_asian']>avg_rate_asian,'large','small')
        print(mw)
        Midwest.midwest = mw

    def menu_5(self):
        Midwest.midwest['size_popasian'].value_counts().plot.bar(rot = 0)
        plt.savefig(MIDWEST_SAVE_CTX+'midwest_graph.jpg')

if __name__ == "__main__":
    m = Midwest()
    while True:
        print("*"*100)
        menu = ["종료",
                "메타데이터 출력",
                "poptotal/popasian 변수를 total/asian로 이름변경",
                "전체 인구 대비 아시아 인구 백분율 변수 추가",
                "아시아 인구 백분율 전체 평균을 large/small 로 분류",
                "large/small 빈도표와 빈도막대그래프 작성"]
        for i, j in enumerate(menu):
            print(f'{i}.{j}')
        choice = int(input('메뉴 입력 : '))
        print("*"*100)
        if choice == 0:
            print("종료")
            break
        elif choice == 1:
            print("메타데이터 출력")
            m.menu_1()
        elif choice == 2:
            print("poptotal/popasian 변수를 total/asian로 이름변경")
            m.menu_2()
        elif choice == 3:
            print("전체 인구 대비 아시아 인구 백분율 변수 추가")
            m.menu_3()
        elif choice == 4:
            print("아시아 인구 백분율 전체 평균을 large/small 로 분류")
            m.menu_4()
        elif choice == 5:
            print("large/small 빈도표와 빈도막대그래프 작성")
            m.menu_5()
        else:
            print(" 잘못된 메뉴 입력 ")