from bs4 import BeautifulSoup

html = '<td class="title">'\
'<div class="tit3">'\
'<a href="/movie/bi/mi/basic.nhn?code=159892" title="탐정: 리턴즈">탐정: 리턴즈</a>'\
'</div>'\
'</td>'

def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    print("bs:", bs)
    print("bs.td:", bs.td)
    print("bs.a:", bs.a)
    print("bs.td.div:", bs.td.div)

    print("bs.div.attrs:",bs.div.attrs)

# attrs
def ex2():
    bs = BeautifulSoup(html, 'html.parser')
    print("bs.div.attrs:",bs.div.attrs)
    print("bs.find(bs.div.attrs):",bs.find(bs.div.attrs))

# attrs.elements
def ex3():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.find('td', attrs={'class': 'title'})
    print(tag)

    tag = bs.find(attrs={'class': 'tit3'})
    print(tag)

if __name__ == '__main__':
    ex3()


