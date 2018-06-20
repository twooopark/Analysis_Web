import collection
# import analyze
# import visualize
# from config import CONFIG

# 처리하는 함수를 만들어서, 내부에서 처리하게끔 해보자
def proc(html):
    print("processing..."+html)

def store(result):
    pass

if __name__ == '__main__':
    result = collection.crawling(
                url='http://movie.naver.com/movie/sdb/rank/rmovie.nhn',
                encoding='cp949',
                proc=proc,
                store=store)
