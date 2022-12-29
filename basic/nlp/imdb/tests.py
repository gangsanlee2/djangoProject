from basic.nlp.imdb.services import NaverMovieService

if __name__ == '__main__':
    result = NaverMovieService().process("시간 아깞다. 정말 쓰레기 영화다")
    result = '{:.2%}'.format(result)
    print(f'긍정률 : {result}')