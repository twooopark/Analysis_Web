from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

request = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
response = urlopen(request)
html = response.read().decode('cp949')
# print(html)

bs = BeautifulSoup(html, 'html.parser')
# print(bs.prettify())

tags = bs.findAll('div', attrs={'class': 'tit3'})

# a태그 안에 내용(text)
# for tag in tags:
#     print(tag.a.text)

# + 넘버링
for index, tag in enumerate(tags):
    print(index, tag.a.text, tag.a['href'], sep=' : ')