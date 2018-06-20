from itertools import count
from itertools import count
from collection import crawling
from bs4 import BeautifulSoup
import pandas as pd
from collection.data_dict import sido_dict, gungu_dict
import os
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
    results = []
    for page in range(1,3): #count(start=1):
        #range(115,123):   # page값은 1부터 계속 상승... 내부에서 break
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
            strs = list(tag_tr.strings)
            # print(strs)
            name = strs[1]
            addr = strs[3]
            sidogu = strs[3].split(" ")[:2]
            # print(addr)

            results.append( (name, addr)+tuple(sidogu) )
            # 튜플을 union 하면서
            # [('황간점', '충청북도 영동군 황간면 남성리 558-1', '충청북도', '영동군'),..]
            # 위와 같은 결과물을 얻음음
    print(results)
    # stroe
    table = pd.DataFrame(results, columns=['name','adderss','sido','gungu'])
    print(table)

    table.to_csv(
        '{0}/pelicana_table.csv'.format('__result__'),# RESULT_DIRECTORY),
        encoding='utf-8',
        mode='w',
        index=True
    )
# 경로가 없으면 만들자
if not os.path.exists('__result__'):
    os.makedirs('__result__')

if __name__ == '__main__':
    # pelicana - 처리, 저장
    crawling_pelicana()