import collection
# import analyze
# import visualize
# from config import CONFIG

# 각 모듈의 에러 메세지를 받아와서 메인에서 출력하도록 한다.
def my_error(e):
    print("myerror: " + str(e))


if __name__ == '__main__':
    result = collection.crawling(
                url='http://movie.naver.com/movie/sdb/rank/rmovie.nh1n',
                encoding='cp949')
                # err=my_error)
                # 원래 기본대로 내부에서 처리하는게 낫다.
    print(result)