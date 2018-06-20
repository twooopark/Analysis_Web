from itertools import count
from collection.data_dict import sido_dict, gungu_dict
from collection.crawler import crawling
from bs4 import BeautifulSoup
import xml.etree.ElementTree as et
import pandas as pd
import urllib
import os

RESULT_DIRECTORY = '__result__/crawling'

def crawling_pelicana():
    results = []
    for page in count(start=1): #range(115,123):
        #  page값은 1부터 계속 상승... 내부에서 break
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
            address = strs[3]
            sidogu = address.split(" ")[:2]
            # print(addr)

            results.append( (name, address)+tuple(sidogu) )
            # 튜플을 union 하면서
            # [('황간점', '충청북도 영동군 황간면 남성리 558-1', '충청북도', '영동군'),..]
            # 위와 같은 결과물을 얻음음
    print('results: ', results)
    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gungu'])
    print('table: ',table)

    # v를 주고, 값을 반환받아 온다
    # v, v는 그냥 v그대로 유지
    # 결론: 만약 v가 없으면 v그대로 없는 상태로 유지
    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v, v))
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))
    print(table)

    table.to_csv(
        '{0}/pelicana_table.csv'.format(RESULT_DIRECTORY),
        encoding='utf-8',
        mode='w',
        index=True
    )

def proc_nene(xml):
    root = et.fromstring(xml)
    results = []
    for el in root.findall('item'): # pandas랑 다르게 소문자 a...
        name = el.findtext('aname1')
        sido = el.findtext('aname2')
        gungu = el.findtext('aname3')
        address = el.findtext('aname5')

        results.append( (name,address,sido,gungu) )
    # print(results)
    return results

def store_nene(data):
    table = pd.DataFrame(data, columns=['name','address','sido','gungu'])
    # print(table)
    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v, v))
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))
    print(table)

    table.to_csv(
        '{0}/nene_table.csv'.format(RESULT_DIRECTORY),
        encoding='utf-8',
        mode='w',
        index=True
    )


# 경로가 없으면 만들자
if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)

if __name__ == '__main__':
    # pelicana - 처리, 저장
    crawling_pelicana()

    # nene
    crawling(
        url='http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'
            % (urllib.parse.quote('전체'), urllib.parse.quote('전체')),
        proc=proc_nene,
        store=store_nene
    )
