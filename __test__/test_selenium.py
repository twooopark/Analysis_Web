from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, UnexpectedAlertPresentException
from bs4 import BeautifulSoup


def crawling_kyochon():
    results = []
    browser = webdriver.Chrome('D:\pythonPycharm\chromedriver');
    url = 'http://www.kyochon.com/shop/domestic.asp?sido1=0&sido2=0&txtsearch='
    browser.get(url)
    browser.find_element_by_id('sido1')
    for sido1 in range(1, 20):  # count(start=1): #, ":", end=" ")
        url = 'http://www.kyochon.com/shop/domestic.asp?sido1=' + str(sido1)
        browser.get(url)
        html = browser.page_source

        bs = BeautifulSoup(html, 'html.parser')
        tag_select = bs.findAll('select')

        print(tag_select)
crawling_kyochon()