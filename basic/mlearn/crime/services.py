'''
위도 latitude 0~90grade NS
경도 longtitude 0~180grade WS
'''
import os

import folium
import googlemaps
import numpy as np
import pandas as pd
from sklearn import preprocessing

from admin.path import dir_path

CRIME_MENUS = ["close",  # 0
               "spec",  # 1
               "save police position",  # 2
               "save cctv position",  # 3
               "save police normalization",  # 4
               "folium example",  # 5
               "save seoul folium",  # 6
               "create folium data"  # 7
               ]

crime_menu = {"1": lambda t: t.spec(),
              "2": lambda t: t.save_police_pos(),
              "3": lambda t: t.save_cctv_pop(),
              "4": lambda t: t.save_police_norm(),
              "5": lambda t: t.folium_example(),
              "6": lambda t: t.save_seoul_folium(),
              "7": lambda t: t.create_folium_data()
              }


class CrimeService:
    def __init__(self):
        self.crime = pd.read_csv(os.path.join(dir_path('crime'), 'data', 'crime_in_seoul.csv'))
        cols = ['절도 발생', '절도 검거', '폭력 발생', '폭력 검거']
        self.crime[cols] = self.crime[cols].replace(',', '', regex=True).astype(int)
        self.cctv = pd.read_csv(os.path.join(dir_path('crime'), 'data', "cctv_in_seoul.csv"))
        self.ls = [self.crime, self.cctv]
        self.pop = pd.read_excel(os.path.join(dir_path('crime'), 'data', "pop_in_seoul.xls"), header=1,
                                 usecols=['자치구', '합계', '한국인', '등록외국인', '65세이상고령자'], skiprows=[2])
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']
        self.us_states = os.path.join(dir_path('crime'), 'data', 'us-states.json')
        self.us_unemployment = pd.read_csv(os.path.join(dir_path('crime'), 'data', 'us_unemployment.csv'))
        self.kr_states = os.path.join(dir_path('crime'), 'data', 'kr-state.json')

    '''
    def temp(self):
        def sub(x):
            print(" --- 1.Shape ---")
            print(x.shape)
            print(" --- 2.Features ---")
            print(x.columns)
            print(" --- 3.Info ---")
            print(x.info())
            print(" --- 4.Case Top1 ---")
            print(x.head(1))
            print(" --- 5.Case Bottom1 ---")
            print(x.tail(3))
            print(" --- 6.Describe ---")
            print(x.describe())
            print(" --- 7.Describe All ---")
            print(x.describe(include='all'))
        return sub

    def spec(self):
        s = self.temp()
        s(self.crime)
        s(self.cctv)
    '''

    def spec(self):
        [(lambda x: print(f" --- 1.Shape ---\n"
                          f"{x.shape}\n"
                          f" --- 2.Features --- \n"
                          f"{x.columns}\n"
                          f" --- 3.Info ---\n"
                          f"{x.info()}\n"
                          f" --- 4.Case Top1 ---\n"
                          f"{x.head(1)}\n"
                          f" --- 5.Case Bottom1 ---\n"
                          f"{x.tail(3)}\n"
                          f" --- 6.Describe ---\n"
                          f"{x.describe()}\n"
                          f" --- 7.Describe All ---\n"
                          f"{x.describe(include='all')}"))(i)
         for i in self.ls]

    def save_police_pos(self):  # nominal
        crime = self.crime
        station_names = []
        for name in crime['관서명']:
            print(f'지역이름: {name}')
            station_names.append(f'서울{str(name[:-1])}경찰서')
        print(f' 서울시내 경찰서는 총 {len(station_names)}개 이다')
        [print(f'{str(i)}') for i in station_names]
        gmaps = (lambda x: googlemaps.Client(key=x))(
            "")  # key key  key key key key key key key key key key key key key key key key key key key key key key key key key key key key key key key key
        print(gmaps.geocode("서울중부경찰서", language='ko'))
        print(' ### API에서 주소추출 시작 ### ')
        station_addrs = []
        station_lats = []
        station_lngs = []
        for i, name in enumerate(station_names):
            _ = gmaps.geocode(name, language='ko')
            print(f'name {i} = {_[0].get("formatted_address")}')
            station_addrs.append(_[0].get('formatted_address'))
            _loc = _[0].get('geometry')
            station_lats.append(_loc['location']['lat'])
            station_lngs.append(_loc['location']['lng'])
        gu_names = []
        for name in station_addrs:
            _ = name.split()
            gu_name = [gu for gu in _ if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        # 구와 경찰서의 위치가 다른 경우 수작업
        crime.loc[crime['관서명'] == '혜화서', ['구별']] = '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] = '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] = '강서구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] = '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] = '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] = '강남구'
        crime.to_csv(os.path.join(dir_path('crime'), 'save', 'police_pos.csv'), index=False)
        crime.to_pickle(os.path.join(dir_path('crime'), 'save', 'police_pos.pkl'))
        df = pd.read_pickle(os.path.join(dir_path('crime'), 'data', 'police_pos.pkl'))
        print(df)

    def save_cctv_pop(self):  # ratio -> nominal
        cctv = self.cctv
        pop = self.pop
        cctv.rename(columns={cctv.columns[0]: '구별'}, inplace=True)
        pop.rename(columns={
            pop.columns[0]: '구별',
            pop.columns[1]: '인구수',
            pop.columns[2]: '한국인',
            pop.columns[3]: '외국인',
            pop.columns[4]: '고령자',
        }, inplace=True)
        pop.drop(index=26, inplace=True)
        pop['외국인비율'] = pop['외국인'].astype(int) / pop['인구수'].astype(int) * 100
        pop['고령자비율'] = pop['고령자'].astype(int) / pop['인구수'].astype(int) * 100
        cctv.drop(['2013년도 이전', '2014년', '2015년', '2016년'], axis=1, inplace=True)
        cctv_pop = pd.merge(cctv, pop, on="구별")
        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])
        print(f'고령자비율과 CCTV의 상관계수 {str(cor1)} \n'
              f'외국인비율과 CCTV의 상관계수 {str(cor2)} ')
        cctv_pop.to_pickle(os.path.join(dir_path('crime'), 'save', "cctv_pop.pkl"))
        """
         고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                     [-0.28078554  1.        ]] 
         외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                     [-0.13607433  1.        ]]
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                    [-0.28078554  1.        ]]
        외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                    [-0.13607433  1.        ]]                        
         """

    def save_police_norm(self):
        police_pos = pd.read_pickle(os.path.join(dir_path('crime'), 'save', 'police_pos.pkl'))
        police = pd.pivot_table(police_pos, index="구별", aggfunc=np.sum)
        police['살인검거율'] = (police['살인 검거'].astype(int) / police['살인 발생'].astype(int)) * 100
        police['강도검거율'] = (police['강도 검거'].astype(int) / police['강도 발생'].astype(int)) * 100
        police['강간검거율'] = (police['강간 검거'].astype(int) / police['강간 발생'].astype(int)) * 100
        police['절도검거율'] = (police['절도 검거'].astype(int) / police['절도 발생'].astype(int)) * 100
        police['폭력검거율'] = (police['폭력 검거'].astype(int) / police['폭력 발생'].astype(int)) * 100
        police.drop(columns={'살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'})
        for i in self.crime_rate_columns:
            police.loc[police[i] > 100, 1] = 100
        police.rename(columns={
            '살인 발생': '살인',
            '강도 발생': '강도',
            '강간 발생': '강간',
            '절도 발생': '절도',
            '폭력 발생': '폭력'
        }, inplace=True)
        x = police[self.crime_rate_columns].values
        min_max_scaler = preprocessing.MinMaxScaler()
        """
        스케일링은 선형변환을 적용하여
        전체 자료의 분포를 평균 0, 분산 1이 되도록 만드는 과정
        """
        x_scaled = min_max_scaler.fit_transform(x.astype(float))  # float -> 연속형
        """
        정규화 normalization
        많은 양의 데이터를 처리함에 있어 데이터의 범위(도메인)를 일치시키거나
        분포(스케일)를 유사하게 만드는 작업
        """
        police_norm = pd.DataFrame(x_scaled, columns=self.crime_columns, index=police.index)
        police_norm[self.crime_rate_columns] = police[self.crime_rate_columns]
        police_norm['범죄'] = np.sum(police_norm[self.crime_rate_columns], axis=1)
        police_norm['검거'] = np.sum(police_norm[self.crime_columns], axis=1)
        police_norm.to_pickle(os.path.join(dir_path('crime'), 'save', 'police_norm.pkl'))
        print(pd.read_pickle(os.path.join(dir_path('crime'), 'save', 'police_norm.pkl')))

    def folium_example(self):
        us_states = self.us_states
        us_unemployment = self.us_unemployment
        '''
        url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
        '''
        geo_data = us_states
        data = pd.read_csv(us_unemployment)
        bins = list(us_unemployment['Unemployment'].quantile([0, 0.25, 0.5, 0.75, 1]))
        map = folium.Map(location=[48, -102], zoom_start=5)
        folium.Choropleth(
            geo_data=geo_data,
            data=data,
            name='choropleth',
            columns=["State", "Unemployment"],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name='Unemployment Rate (%)',
            bins=bins
        ).add_to(map)
        map.save(os.path.join(dir_path('crime'), 'save', "unemployment.html"))

    def save_seoul_folium(self):
        geo_data = self.kr_states
        data = self.create_folium_data()
        map = folium.Map(location=[37.5502, 126.982], zoom_start=12)
        folium.Choropleth(
            geo_data=geo_data,
            data=data,
            name='choropleth',
            columns=["State", "Crime Rate"],
            key_on="feature.id",
            fill_color="PuRd",
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Crime Rate (%)',
        ).add_to(map)
        map.save(os.path.join(dir_path('crime'), 'save', "crime.html"))

    def create_folium_data(self):
        police_pos = pd.read_pickle(os.path.join(dir_path('crime'), 'save', 'police_pos.pkl'))
        police_norm = pd.read_pickle(os.path.join(dir_path('crime'), 'save', 'police_norm.pkl'))
        temp = police_pos[self.arrest_columns] / police_pos[self.arrest_columns].max()
        police_pos['검거'] = np.sum(temp, axis=1)
        return tuple(zip(police_norm.index, police_norm['범죄']))


def set_json_from_df():
    df = pd.read_json(os.path.join(dir_path('crime'), 'data', 'us-states.json'))
    df.drop(df.index[[8, 51]], inplace=True)
    df.to_json(os.path.join(dir_path('crime'), 'save', 'us-states.json'), orient='index')


if __name__ == '__main__':
    def my_menu(ls):
        for i, j in enumerate(ls):
            print(f"{i}. {j}")
        return input('메뉴선택: ')


    if __name__ == '__main__':
        t = CrimeService()
        while True:
            menu = my_menu(CRIME_MENUS)
            if menu == '0':
                print("종료")
                break
            else:
                crime_menu[menu](t)
                try:
                    crime_menu[menu](t)
                except KeyError:
                    print(" ### Error ### ")