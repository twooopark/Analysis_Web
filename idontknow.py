from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

request = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
response = urlopen(request)
html = response.read().decode('cp949')
print(html)

bs = BeautifulSoup(html, 'html.parser')
print(bs.prettify())