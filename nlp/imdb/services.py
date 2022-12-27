import csv

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

class ImdbService(object):
    def __init__(self):
        pass

class NaverMovieService(object):
    def __init__(self):
        pass

    def crawling(self):
        url = f'https://movie.naver.com/movie/point/af/list.naver?&page='
        driver = webdriver.Chrome(r'C:\Users\bitcamp\PycharmProjects\djangoProject\webcrawler\chromedriver.exe')
        file_name = 'naver_movie_review_corpus.csv'
        save_path = r'C:\Users\bitcamp\PycharmProjects\djangoProject\webcrawler\\'
        reviews = []
        ratings = []
        for i in range(1,11):
            driver.get(url+str(i))
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            text = soup.find_all('td', attrs={'class', 'title'})
            ratings += [td.em.string for td in text]
            reviews += [td.br.next_element.strip() for td in text]
        ls = list(zip(reviews,ratings))
        result = []
        for i,j in enumerate(ls):
            if j[0] != '':
                result.append(j[0]+','+j[1])
        ds = pd.Series(result)
        ds.to_csv(save_path+file_name, header=None, index=None)
        print(result)
        print(f'len(ls) is {len(ls)}')

if __name__ == '__main__':
    NaverMovieService().crawling()