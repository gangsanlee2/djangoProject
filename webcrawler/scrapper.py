# db에 저장할거면 모델(도메인) 쓰고 더이상 필요없으면 services에서 함수형으로 사용
import urllib
from dataclasses import dataclass
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

from blog.common import Common

"""
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
"""
"""
class BugsMusic:    #class BugsMusic(object) 파이썬에서 object 생략 가능

    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url),'lxml')
        # print(soup.prettify(encoding="UTF8")) 무작정 추출하면 안됨! -> 원하는 정보만 스크랩하는게 중요!
        _ = 0
        title = {"class":"title"}
        artist = {"class":"artist"}
        titles = soup.find_all(name="p", attrs=title)
        artists = soup.find_all(name="p", attrs=artist)

        '''
        for i in titles: #여기서 titles는 시퀀스 자료구조
            print(f"{i.find('a').text}")
        print("*"*20)
        for i in artists:
            print(f"{i.find('a').text}")
        print("*"*20)
        '''

        for i,j in zip(titles,artists):
            _ += 1
            print(f"{_}위 {i.find('a').text} - {j.find('a').text}")
"""

'''
@dataclass
class Scrap:
    html: str
    parser: str
    domain: str
    query_string: str
    headers: dict
    tag_name: str
    fname: str
    class_names: []
    artists: []
    titles: []
    diction: {}
    df: None
    soup: BeautifulSoup

    @property
    def html(self): return self._html

    @html.setter
    def html(self, html): self._html = html

    @property
    def parser(self): return self._parser

    @parser.setter
    def parser(self, parser): self._parser = parser

    @property
    def domain(self): return self._domain

    @domain.setter
    def domain(self, domain): self._domain = domain

    @property
    def query_string(self): return self._query_string

    @query_string.setter
    def query_string(self, query_string): self._query_string = query_string

    @property
    def headers(self): return self._headers

    @headers.setter
    def headers(self, headers): self._headers = headers

    @property
    def tag_name(self): return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name): self._tag_name = tag_name

    @property
    def fname(self): return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def class_names(self): return self._class_names

    @class_names.setter
    def class_names(self, class_names): self._class_names = class_names

    @property
    def artists(self): return self._artists

    @artists.setter
    def artists(self, artists): self._artists = artists

    @property
    def titles(self): return self._titles

    @titles.setter
    def titles(self, titles): self._titles = titles

    @property
    def diction(self): return self._diction

    @diction.setter
    def diction(self, diction): self._diction = diction

    @property
    def df(self): return self._df

    @df.setter
    def df(self, df): self._df = df

    @property
    def soup(self) -> BeautifulSoup: return self._soup

    @soup.setter
    def soup(self, soup): self._soup = soup

    def dict_to_dataframe(self):
        print(len(self.diction))
        self.df = pd.DataFrame.from_dict(self.diction, orient='index')

    def dataframe_to_csv(self):
        path = './save/result.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)
'''

@dataclass
class Scrap:
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
        path = '../../../../static/save/cop/scp/service/scrapper/fake_melon_rank.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)


def BugsMusic(arg):
    soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), 'lxml')
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i + 1}위 {j} : {k}")  # 디버깅
     for i, j, k in zip(range(0, len(titles)), titles, artists)]
    diction = {}  # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv()  # csv파일로 저장


def MelonMusic(arg):
    req = urllib.request.Request(arg.domain + arg.query_string, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req), 'lxml')
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i + 1}위 {j} : {k}")  # 디버깅
     for i, j, k in zip(range(0, len(titles)), titles, artists)]
    diction = {}  # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv()  # csv파일로 저장


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