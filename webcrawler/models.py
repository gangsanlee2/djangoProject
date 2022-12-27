# db에 저장할거면 모델(도메인) 쓰고 더이상 필요없으면 services에서 함수형으로 사용
from dataclasses import dataclass

import pandas as pd
from bs4 import BeautifulSoup

from webcrawler.common import Common
from webcrawler.scrapper import BugsMusic, MelonMusic, Scrap


@dataclass
class ScrapVO:
    html = ''
    parser = ''
    domain = ''
    query_string = ''
    headers = {}
    tag_name = ''
    fname = ''
    class_names = []
    artists = []
    titles = []
    diction = {}
    df = None
    soup = BeautifulSoup

    def dict_to_dataframe(self):
        print(len(self.diction))
        self.df = pd.DataFrame.from_dict(self.diction, orient='index')

    def dataframe_to_csv(self):
        path = r'C:\Users\bitcamp\PycharmProjects\djangoProject\webcrawler\save\melon_rank.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)


class ScrapController(object):

    @staticmethod
    def menu_1(arg):
        BugsMusic(arg)

    @staticmethod
    def menu_2(arg):
        MelonMusic(arg)


if __name__ == '__main__':
    api = ScrapController()
    scrap = Scrap()
    while True:
        menus = ["종료", "벅스 뮤직", "멜론"]
        menu = Common.menu(menus)
        if menu == "0":
            print(menus[0])
            break
        elif menu == "1":
            print(menus[1])
            scrap.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            scrap.query_string = "20221101"
            scrap.parser = "lxml"
            scrap.class_names = ["title", "artist"]
            scrap.tag_name = "p"
            scrap.path = './save/result.csv'
            api.menu_1(scrap)
        elif menu == "2":
            print(menus[2])
            scrap.domain = "https://www.melon.com/chart/index.htm?dayTime=2022110817"
            scrap.query_string = "2022110817"
            scrap.parser = "lxml"
            scrap.class_names = ["ellipsis rank01", "ellipsis rank02"]
            scrap.tag_name = "div"
            scrap.path = './save/result.csv'
            api.menu_2(scrap)
        else:
            print(" ### 해당 메뉴 없음 ### ")