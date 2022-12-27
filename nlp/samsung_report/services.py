from konlpy.tag import Okt

from nlp.samsung_report.models import Entity
import nltk
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

class Service:
    def __init__(self):
        self.texts = []
        self.tokens = []
        self.stopwords = []
        self.freqtxt = []
        self.okt = Okt()


    def extract_tokens(self, payload):
        #print(' text 문서에서 token 추출')
        filename = payload.context + payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.texts = f.read()
        #print(f'{self.texts[:300]}')
        #print('####################################################################################################')

    def extract_hangeul(self):
        #print('한글 추출')
        texts = self.texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ ㄱ-힣]')
        self.texts = tokenizer.sub('', texts)
        #print(f'{self.texts[:300]}')
        #print('####################################################################################################')

    def conversion_token(self):
        #print('토큰으로 변환')
        self.tokens = word_tokenize(self.texts)
        #print(f'{self.tokens[:300]}')
        #print('####################################################################################################')

    def compound_noun(self):
        #print('복합명사는 묶어서 filtering 으로 출력')
        #print('예: 삼성전자의 스마트폰은 --> 삼성전자 스마트폰')
        noun_tokens = []
        for token in self.tokens:
            token_pos = self.okt.pos(token)
            temp = [txt_tag[0] for txt_tag in token_pos
                    if txt_tag[1] == 'Noun']
            if len("".join(temp)) > 1:
                noun_tokens.append("".join(temp))
        self.texts = " ".join(noun_tokens)
        #print(f'{self.texts[:300]}')
        #print('####################################################################################################')

    def extract_stopword(self, payload):
        #print('스톱워드 추출')
        filename = payload.context + payload.fname
        with open(filename, 'r', encoding='utf-8') as f:
            self.stopwords = f.read()
        self.stopwords = self.stopwords.split(' ')
        #print('####################################################################################################')

    def filtering_text_with_stopword(self):
        #print('스톱워드 필터링')
        self.texts = word_tokenize(self.texts)
        self.texts = [text for text in self.texts
                      if text not in self.stopwords]
        #print(f'{self.texts[:300]}')
        #print('####################################################################################################')

    def frequent_text(self):
        #print('빈도수로 정렬')
        self.freqtxt = pd.Series(dict(FreqDist(self.texts))).sort_values(ascending=False)
        #print(f'{self.freqtxt[:100]}')
        return self.freqtxt
        #return dict(FreqDist(self.texts))


    def draw_wordcloud(self, payload):
        print('워드 크라우드 생성')
        filename = payload.context + payload.fname
        wcloud = WordCloud(filename,
                           relative_scaling=0.2,
                           background_color='white').generate(" ".join(self.texts))

        plt.figure(figsize=(12, 12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
        print('####################################################################################################')


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def download_dictionary(self):
        # nltk.download('all') all로 하면 너~무 오래 걸림
        nltk.download('punkt')

    def data_analysis(self):
        self.download_dictionary()
        self.entity.fname = 'kr-Report_2018.txt'
        self.entity.context = 'C:/Users/bitcamp/PycharmProjects/djangoProject/nlp/samsung_report/'
        self.service.extract_tokens(self.entity)
        self.service.extract_hangeul()
        self.service.conversion_token()
        self.service.compound_noun()
        self.entity.fname = 'stopwords.txt'
        self.service.extract_stopword(self.entity)
        self.service.filtering_text_with_stopword()
        self.service.frequent_text()
        self.entity.fname = 'D2Coding.ttf'
        self.service.draw_wordcloud(self.entity)

    def hook(self):
        self.entity.fname = 'kr-Report_2018.txt'
        self.entity.context = 'C:/Users/bitcamp/PycharmProjects/djangoProject/nlp/samsung_report/'
        self.service.extract_tokens(self.entity)
        self.service.extract_hangeul()
        self.service.conversion_token()
        self.service.compound_noun()
        self.entity.fname = 'stopwords.txt'
        self.service.extract_stopword(self.entity)
        self.service.filtering_text_with_stopword()
        data_series = self.service.frequent_text()
        ls = []
        [ls.append({'word': data_series.index[i], 'freq': str(data_series[data_series.index[i]])}) for i in range(len(data_series))]
        #print(ls)
        #print(f'data_series.index[0] is {type(data_series.index[0])}\n'
              #f'data_series[data_series.index[0]] is {type(str(data_series[data_series.index[0]]))}')
        return ls

if __name__ == '__main__':
    Controller().hook()