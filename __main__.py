from itertools import count
from collection.data_dict import sido_dict, gungu_dict
from collection.crawler import crawling
from bs4 import BeautifulSoup
from datetime import datetime
import urllib
import sys
import xml.etree.ElementTree as et
import pandas as pd
import os


RESULT_DIRECTORY = '__result__/crawling'

def crawling_pelicana():
    results = []
    #  page값은 1부터 계속 상승... 내부에서 break
    for page in count(start=1):
        print(page, ":", end=" ")
        url='http://pelicana.co.kr/store/stroe_search.html?page='+str(page)+'&branch_name=&gu=&si='
        html = crawling(url=url)
        bs = BeautifulSoup(html, 'html.parser')

        tag_table = bs.find('table', attrs={"class":"table mt20"})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 마지막 페이지
        if len(tags_tr) == 0 :
            break;

        # tuple로 변환
        for tag_tr in tags_tr:
            strs = list(tag_tr.strings)
            name = strs[1]
            address = strs[3]
            sidogu = address.split(" ")[:2]

            # 튜플을 union 하면서 아래와 같은 결과물을 얻음
            # [('황간점', '충청북도 영동군 황간면 남성리 558-1', '충청북도', '영동군'), ...]
            results.append( (name, address)+tuple(sidogu) )

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gungu']) # columns 순서 주의

    # sido_dict는 다음과 같은 dictionary 이다. {'서울시': '서울특별시', '서울': '서울특별시', '강원': '강원도 ... }
    # dictionary.values = dictionary.get(dictionary.keys)
    # sido_dict.get('서울시')를 하면, '서울시'는 key 이므로, value인 '서울특별시'가 반환된다.
    # get(v, v) --> 만약 key값 v가 없으면, v를 그대로 반환한다.
    # sido_dict.get(v, v) by passing an anonymous function as an argument to Series.apply().
    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v, v))
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))

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
    return results

def store_nene(data):
    table = pd.DataFrame(data, columns=['name','address','sido','gungu'])
    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v, v))
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))
    print(table)

    table.to_csv(
        '{0}/nene_table.csv'.format(RESULT_DIRECTORY),
        encoding='utf-8',
        mode='w',
        index=True
    )

def crawling_kyochon(
        err=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)
        ):
    results = []
    for sido1 in range(1, 17):
        for sido2 in count(start=1):
            print(sido1, ", ",sido2," :", end=" ")
            url = 'http://www.kyochon.com/shop/domestic.asp?sido1='+str(sido1)+'&sido2='+str(sido2)+'&txtsearch='
            html = crawling(url=url)
            if html is None :
                break;
            try:
                bs = BeautifulSoup(html, 'html.parser')
                tag_div = bs.find('div', attrs={'class': 'shopSchList'})
                tags_dl = tag_div.findAll('dl')
                for tag_dl in tags_dl:
                    name = tag_dl.find('dt').text
                    address = tag_dl.find('dd').text.strip().replace("\t","").split("\r\n")[0]
                    sido = address.split()[0]
                    gungu = address.split()[1]

                    results.append( (name,address,sido,gungu) )
            except AttributeError as e:
                err(e)

    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gungu'])
    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v, v))
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))
    table.to_csv(
        '{0}/kyochon_table.csv'.format(RESULT_DIRECTORY),
        encoding='utf-8', mode='w', index=True)


def crawling_bbq(
        err=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)
        ):
    results = []

    url = 'https://www.bbq.co.kr/page/order/store-search_left.asp?lat=37.491872&lng=127.115922&schval=%s' % ( urllib.parse.quote('점') )
    html = crawling(url=url)

    try:
        bs = BeautifulSoup(html, 'html.parser')
        tags_div = bs.findAll('div', attrs={'class': 'storeNearyByItem-title'})
        items = bs.findAll('div', attrs={'class': 'storeNearyByItem-address'})
        for i in range(len(tags_div)):
            name = tags_div[i].find('span').text
            address = items[i].text.strip()
            sido = address.split()[0]
            gungu = address.split()[1]
            print(address)
            results.append((name, address, sido, gungu))
    except AttributeError as e:
        err(e)

    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gungu'])
    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v, v))
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))
    table.to_csv(
        '{0}/bbq_table.csv'.format(RESULT_DIRECTORY),
        encoding='utf-8', mode='w', index=True)



# 경로가 없으면 만들자
if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)

if __name__ == '__main__':
    # pelicana
    crawling_pelicana()


    # nene
    crawling(
        url='http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'
            % (urllib.parse.quote('전체'), urllib.parse.quote('전체')),
        proc=proc_nene,
        store=store_nene)

    # kyochon
    crawling_kyochon()

    # bbq
    crawling_bbq()