from urllib.request import Request, urlopen

request = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
response = urlopen(request)
html = response.read().decode('cp949')
print(html)