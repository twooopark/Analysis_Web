from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, UnexpectedAlertPresentException
from bs4 import BeautifulSoup
import time


def crawling_goobne():
    results = []
    url = 'https://www.goobne.co.kr/store/search_store.jsp'

    # 첫 페이지 로딩
    browser = webdriver.Chrome('D:\pythonPycharm\chromedriver');
    browser.get(url)
    # wait page loading...
    time.sleep(5)

    html = browser.page_source
    print(html)

    for page in range(2, 5):
        # 자바스크립트 실행
        script = 'store.getList(%d)' %page
        browser.execute_script(script)
        time.sleep(2)

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

crawling_goobne()