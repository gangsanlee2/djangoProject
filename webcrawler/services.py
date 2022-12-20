import csv
import os
import urllib
from urllib.request import urlopen

#from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from webcrawler.models import ScrapVO

import pandas as pd
from bs4 import BeautifulSoup

class ScrapService(ScrapVO):
    def __init__(self):
        global driverpath, naver_url, savepath, charset, encoding
        driverpath = r'C:\Users\bitcamp\PycharmProjects\djangoProject\webcrawler\chromedriver'
        savepath = r'C:\Users\bitcamp\PycharmProjects\djangoProject\webcrawler\save\movie_rank.csv'
        naver_url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
        encoding = 'UTF-8'

    def bugs_music(self): # 기본크롤링
        soup = BeautifulSoup(urlopen(self.domain + self.query_string), 'lxml')
        title = {"class": self.class_names[0]}
        artist = {"class": self.class_names[1]}
        titles = soup.find_all(name=self.tag_name, attrs=title)
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name=self.tag_name, attrs=artist)
        artists = [i.find('a').text for i in artists]
        [print(f"{i + 1}위 {j} : {k}")  # 디버깅
         for i, j, k in zip(range(0, len(titles)), titles, artists)]
        diction = {}  # dict 로 변환
        for i, j in enumerate(titles):
            diction[j] = artists[i]
        self.diction = diction
        self.dict_to_dataframe()
        self.dataframe_to_csv()  # csv파일로 저장

    def melon_music(self):
        req = urllib.request.Request(self.domain + self.query_string, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(urlopen(req), 'lxml')
        title = {"class": self.class_names[0]}
        artist = {"class": self.class_names[1]}
        titles = soup.find_all(name=self.tag_name, attrs=title)
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name=self.tag_name, attrs=artist)
        artists = [i.find('a').text for i in artists]
        [print(f"{i + 1}위 {j} : {k}")  # 디버깅
         for i, j, k in zip(range(0, len(titles)), titles, artists)]
        diction = {}  # dict 로 변환
        for i, j in enumerate(titles):
            diction[j] = artists[i]
        self.diction = diction
        self.dict_to_dataframe()
        self.dataframe_to_csv()  # csv파일로 저장

    def naver_movie_review(self):
        if os.path.isfile(savepath):
            df = pd.read_csv(savepath)
            return df.columns[0]
        else:
            driver = webdriver.Chrome(driverpath)
            driver.get(naver_url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            all_divs = soup.find_all('div', attrs={'class', 'tit3'})
            products = [[div.a.string for div in all_divs]]
            with open(savepath, 'w', newline='', encoding=encoding) as f:
                wr = csv.writer(f)
                wr.writerows(products)
            driver.close()
            return products[0][0]

if __name__ == '__main__':
    s = ScrapService()
    s.naver_movie_review()