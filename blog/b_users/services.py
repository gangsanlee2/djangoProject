import pandas as pd
from faker import Faker
# pip install pymysql
# pip install sqlalchemy
import pymysql
from sqlalchemy import create_engine
# MySQL Connector using pymysql => 이유는 모르겠지만 아래 두줄 때문에 runserver 안됨
#pymysql.install_as_MySQLdb()
#import MySQLdb

class UserService(object):
    def __init__(self):
        pass

    #b_user_id, email, nickname, password
    def create_users(self):
        f = Faker()

        #b_user_id = [i for i in range(100)]        b_user_id는 autoincrement이므로 만들면 안됨!!!
        email = [f'{f.word()}@gmail.com' for i in range(100)]
        nickname = [f.name() for i in range(100)]
        password = ["root" for i in range(100)]
        df = pd.DataFrame({#'b_user_id': b_user_id,
                      'email': email,
                      'nickname': nickname,
                      'password': password})
        print(f'email 중복 확인 : \n{df.duplicated(["email"], keep="first")}')
        print(df.duplicated(["email"], keep="first").count('True'))
        print(f'email 중복 확인 : \n{df.duplicated(["nickname"], keep="first")}')
        '''
        # {} 안에 해당하는 정보 넣기. {}는 지우기.
        engine = create_engine("mysql+pymysql://root:root@localhost:3306/mydb", encoding='utf-8')
        conn = engine.connect()

        # MySQL에 저장하기
        # 변수명은 이전에 만든 데이터프레임 변수명
        # name은 생성할 테이블명
        # index=False, 인덱스 제외
        df.to_sql(name='b_users', con=engine, if_exists='append', index=False)

        df_read = pd.read_sql_table('b_users', con=conn)
        print(df_read)
        '''
if __name__ == '__main__':
    UserService().create_users()