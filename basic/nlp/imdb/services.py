import os
from collections import defaultdict
from math import log, exp

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

from admin.path import dir_path


class ImdbService(object):
    def __init__(self):
        pass

class NaverMovieService(object):
    def __init__(self):
        global url, driver_path, file_name, save_path, review_train, encoding, k
        url = f'https://movie.naver.com/movie/point/af/list.naver?&page='
        driver_path = os.path.join(dir_path("webcrawler"),'chromedriver.exe')
        file_name = os.path.join(dir_path("imdb"),"data","naver_movie_review_corpus.csv")
        review_train = os.path.join(dir_path("imdb"),"data","review_train.csv")
        save_path = os.path.join(dir_path("imdb"),"data")
        encoding = 'UTF-8'
        k = 0.5
        self.word_probs = []

    def process(self, new_review):
        service = NaverMovieService()
        service.model_fit()
        result = service.classify(new_review)
        return result

    def crawling(self):
        if os.path.isfile(save_path+file_name):
            df = pd.read_csv(save_path+file_name)
            print(df)
        else:
            driver = webdriver.Chrome(driver_path)
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

    def load_corpus(self):
        corpus = pd.read_table(review_train, sep=",", encoding=encoding)
        corpus = np.array(corpus)
        return corpus

    def count_words(self, train_X):
        counts = defaultdict(lambda : [0,0])
        for doc, point in train_X:
            if self.isNumber(doc) is False:
                words = doc.split()
                for word in words:
                    counts[word][0 if point > 3.5 else 1] += 1
        return counts

    def isNumber(self, param):
        try:
            float(param)
            return True
        except ValueError:
            return False

    def probability(self, word_probs, doc):
        docwords = doc.split()
        log_prob_if_class0 = log_prob_if_class1 = 0.0
        for word, prob_if_class0, prob_if_class1 in word_probs:
            if word in docwords:
                log_prob_if_class0 += log(prob_if_class0)
                log_prob_if_class1 += log(prob_if_class1)
            else:
                log_prob_if_class0 += log(1.0 - prob_if_class0)
                log_prob_if_class1 += log(1.0 - prob_if_class1)
        prob_if_class0 = exp(log_prob_if_class0)
        prob_if_class1 = exp(log_prob_if_class1)
        return prob_if_class0 / (prob_if_class0 + prob_if_class1)

    def word_probablities(self, counts, n_class0, n_class1, k):
        return [(w,
                 (class0 + k) / (n_class0 + 2 * k),
                 (class1 + k) / (n_class1 + 2 * k))
                for w, (class0, class1) in counts.items()]

    def classify(self, doc):
        return self.probability(word_probs=self.word_probs, doc=doc)

    def model_fit(self):
        train_X = self.load_corpus()
        '''
        '재밌네요': [1,0]
        '별로 재미없어요': [0,1]
        '''
        num_class0 = len([1 for _, point in train_X if point > 3.5])
        num_class1 = len(train_X) - num_class0
        word_counts = self.count_words(train_X)
        self.word_probs = self.word_probablities(word_counts, num_class0, num_class1, k)


