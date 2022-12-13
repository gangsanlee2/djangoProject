import pandas as pd


class Iris(object):
    def __init__(self):
        self.iris = pd.read_csv(r'C:\Users\bitcamp\PycharmProjects\djangoProject\shop\flower\data\Iris.csv')

    def hook(self):
        pass

    def spec(self):
        print(" --- 1.Shape ---")
        print(self.iris.shape)
        print(" --- 2.Features ---")
        print(self.iris.columns)
        print(" --- 3.Info ---")
        print(self.iris.info())
        print(" --- 4.Case Top1 ---")
        print(self.iris.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.iris.tail(3))
        print(" --- 6.Describe ---")
        print(self.iris.describe())
        print(" --- 7.Describe All ---")
        print(self.iris.describe(include='all'))
        '''
        (150, 6)
        ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
        '''


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
        i = Iris()
        while True:
            print("####################################################################################################")
            choice = my_menu(MENUS)
            print("####################################################################################################")
            if choice == '0':
                print("종료")
                break
            else:
                menu[choice](i)