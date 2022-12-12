from string import ascii_lowercase

import numpy as np
import pandas as pd

'''
class Fruits(object):

    def __init__(self, name, won):
        self.name = name
        self.won = won

    def __str__(self):
        return f"{self.name} {self.won}"

    @staticmethod
    def print_result(ls):
        print(" ### 과일가게 ### ")
        print("***************************")
        print("이름   가격")
        print("***************************")
        for i in ls:
            print(i)
        print("***************************")

    @staticmethod
    def new_fruits():
        return Fruits(input(" 이름 : "), int(input(" 가격 : ")))
'''

def new_fruits_df():
    ls_th = ['제품','가격','판매량']
    ls_name = ['사과','딸기','수박']
    ls_price = [1800,1500,3000]
    ls_amount = [24,38,13]
    ls_tb = [ls_name,ls_price,ls_amount]
    '''
    dc = {}
    for i,j in enumerate(ls_th):
        dc[j] = ls_tb[i]
    '''
    # pythonic by comprehension
    dc = {j : ls_tb[i] for i,j in enumerate(ls_th)}

    df = pd.DataFrame(dc)

    print(dc)
    print('*' * 20)
    print(df)
    print('*' * 20)
    print(f'평균 가격 : {int(df["가격"].mean())}')
    print('*' * 20)
    print(f"평균 판매량 : {int(df['판매량'].mean())}")

def new_number_2d():
    print(pd.DataFrame(np.array([list(range(1,11)),
                                 list(range(11,21)),
                                 list(range(21,31))]),
                       columns=list(ascii_lowercase)[:10]))     # <-> ascii_uppercase


if __name__ == "__main__":
    while True:
        menu = ['종료','과일2D','숫자2D']
        print('*'*100)
        [print(f'{i}.{j}') for i,j in enumerate(menu)]
        choice = int(input('메뉴선택:'))
        print('*' * 100)
        if choice == 0:
            print('종료')
            break
        elif choice == 1:
            print('과일2D')
            new_fruits_df()
        elif choice == 2:
            print('숫자2D')
            new_number_2d()
        else:
            print('잘못된 메뉴 입력')
