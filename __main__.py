from itertools import count
from collection import crawling
from bs4 import BeautifulSoup
# import analyze
# import visualize
# from config import CONFIG


# # 처리하는 함수를 만들어서, 내부에서 처리하게끔 해보자
# def proc(html):
#     print("processing..."+html)
#
# def store(result):
#     pass
#
# result = collection.crawling(
#             url='http://movie.naver.com/movie/sdb/rank/rmovie.nhn',
#             encoding='cp949',
#             proc=proc,
#             store=store)

def crawling_pelicana():
    for page in range(115,123): #count(start=1):  # page값은 1부터 계속 상승... 내부에서 break
        url='http://pelicana.co.kr/store/stroe_search.html?page='+str(page)+'&branch_name=&gu=&si='
        html = crawling(url=url)

        bs = BeautifulSoup(html, 'html.parser')

        tag_table = bs.find('table', attrs={"class":"table mt20"})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        print(page, ":",len(tags_tr))
        # 마지막 페이지
        if len(tags_tr) == 0 :
            break;

        for tag_tr in tags_tr:
            print(list(tag_tr.strings))


if __name__ == '__main__':
    # pelicana - 처리, 저장
    crawling_pelicana()