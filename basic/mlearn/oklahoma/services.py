import os.path

import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

from admin.path import dir_path

oklahoma_meta = {"ACCESS":"ACCESS","ACR":"ACR","AGEP":"나이","BATH":"BATH","BDSP":"침실수","BLD":"건물타입","CONP":"월 수선비",
               "COW":"COW","ELEP":"월 전기료","FESRP":"FESRP","FKITP":"FKITP","FPARC":"FPARC","FSCHP":"FSCHP","FTAXP":"FTAXP",
               "GASP":"월 가스비","HHL":"HHL","HHT":"HHT","HINCP":"가계 소득","LANX":"LANX","MAR":"MAR","MV":"MV",
               "NRC":"자녀 수","R18":"R18","R65":"R65","RAC1P":"RAC1P","RMSP":"방 수","RWAT":"RWAT","SCH":"SCH",
               "SCHL":"SCHL","SEX":"SEX","VALP":"주택가격","VALP_B1":"주택가격등급"}

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5110 entries, 0 to 5109
Data columns (total 12 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 5110 non-null   int64  
 1   gender             5110 non-null   object 
 2   age                5110 non-null   float64
 3   hypertension       5110 non-null   int64  
 4   heart_disease      5110 non-null   int64  
 5   ever_married       5110 non-null   object 
 6   work_type          5110 non-null   object 
 7   Residence_type     5110 non-null   object 
 8   avg_glucose_level  5110 non-null   float64
 9   bmi                4909 non-null   float64
 10  smoking_status     5110 non-null   object 
 11  stroke             5110 non-null   int64  
dtypes: float64(3), int64(4), object(5)
memory usage: 479.2+ KB
None
'''

class OklahomaService:
    def __init__(self):
        self.oklahoma = pd.read_csv(os.path.join(dir_path('oklahoma'), 'data', "comb32.csv"))
        self.comb = None
        self.my_oklahoma = None
        self.df = pd.read_csv(os.path.join(dir_path('oklahoma'), 'save', "oklahoma.csv"))
        self.okl = pd.read_csv(os.path.join(dir_path('oklahoma'), 'save', "oklahoma-final.csv"))
        self.data = None
        self.label = None

    def spec(self):
        print(" --- 1.Shape ---")
        print(self.oklahoma.shape)
        print(" --- 2.Features ---")
        print(self.oklahoma.columns)
        print(" --- 3.Info ---")
        print(self.oklahoma.info())
        print(" --- 4.Case Top1 ---")
        print(self.oklahoma.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.oklahoma.tail(3))
        print(" --- 6.Describe ---")
        print(self.oklahoma.describe())
        print(" --- 7.Describe All ---")
        print(self.oklahoma.describe(include='all'))

    def rename_meta(self):
        self.spec()
        self.my_oklahoma = self.oklahoma.rename(columns=oklahoma_meta)

    '''
    "AGEP":"나이","BDSP":"침실수","CONP":"월 수선비","ELEP":"월 전기료","GASP":"월 가스비"
    "HINCP":"가계 소득","NRC":"자녀 수","RMSP":"방 수","VALP":"주택가격"
    '''
    def interval_variables(self):
        self.rename_meta()
        self.my_oklahoma.drop('월 수선비', axis=1, inplace=True)
        df = self.my_oklahoma
        c1 = df['월 전기료'] <= 500
        c2 = df['월 가스비'] <= 311
        c3 = df['가계 소득'] <= 320000
        self.my_oklahoma = df[c1 & c2 & c3]
        self.my_oklahoma.to_csv(os.path.join(dir_path('oklahoma'), 'save', "oklahoma.csv"),index=False)
        print(self.my_oklahoma.shape)
        print(self.my_oklahoma.info())
    '''
    프리프로세스 종료
    '''

    def ratio_variables(self):
        pass

    def nominal_variables(self):
        df = self.df
        cols = ["COW","FPARC","LANX","SCH","SCHL"]
        df[cols] = df[cols].fillna(0).astype(np.int64)
        df.to_csv(os.path.join(dir_path('oklahoma'), 'save', 'oklahoma-all.csv'), index=False)
        df1 = df.drop(['주택가격'],axis=1)
        df1.to_csv(os.path.join(dir_path('oklahoma'), 'save', 'oklahoma-final.csv'), index=False)

    def ordinal_variables(self):
        pass

    def target(self):
        okl = self.okl
        self.data = okl.drop(['주택가격등급'],axis=1)
        self.label = okl['주택가격등급']
        print(self.data.shape)
        print(self.label.shape)
        print(self.label.value_counts())

    def partition(self):
        self.target()
        X_train, X_test, y_train, y_test = train_test_split(self.data, self.label, test_size=0.5, random_state=42)
        print(X_train.shape)
        print(X_test.shape)
        print(y_train.shape)
        print(y_test.shape)
