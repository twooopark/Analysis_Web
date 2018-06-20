# Analysis_Web
---
> 유명 프랜차이즈 치킨 매장을 찾습니다. 그리고 분포도를 파악합니다.

***Analysis_Web*** 는 몇몇의 매장 사이트를 통해, 매장 정보를 크롤링합니다.
[지점명, 주소, 시도, 군구] 4가지 속성을 추출하여 브랜드명_table.csv 로 저장합니다.

# 치킨 브랜드 별, 매장 탐색 방식
> BBQ
---
<img src="https://github.com/twooopark/Analysis_Web/blob/master/bbq.PNG" height="500px" />

BBQ 매장찾기 : [https://www.bbq.co.kr/page/order/store-search.asp](https://www.bbq.co.kr/page/order/store-search.asp)
매장찾기 기능에서, 모든 매장은 '~점'이라는 지점명을 가지고 있습니다.
이 특징을 이용해서 매장명을 '점'으로 검색해봤습니다. [링크](https://www.bbq.co.kr/page/order/store-search_left.asp?lat=37.491872&lng=127.115922&schval=%EC%A0%90)
1400개 가량의 매장이 검색되었습니다.

> 페리카나
---
<img src="https://github.com/twooopark/Analysis_Web/blob/master/pelic.PNG" height="500px" />

페리카나 매장찾기 : [http://pelicana.co.kr/store/stroe_search.html?page=&branch_name=&gu=&si=](http://pelicana.co.kr/store/stroe_search.html?page=&branch_name=&gu=&si=)
매장 찾기 기능에서, 매장 리스트의 모든 페이지를 완전탐색하여 모든 매장을 찾습니다.


> 네네치킨
<img src="https://github.com/twooopark/Analysis_Web/blob/master/nene.PNG" height="500px" />

제공받은 URL을 통해 XML형식으로 데이터를 받았고, xml.etree.ElementTree을 이용해 파싱했습니다.


> 교촌치킨
<img src="https://github.com/twooopark/Analysis_Web/blob/master/kyochon.PNG" height="500px" />

교촌치킨 매장찾기 [http://www.kyochon.com/shop/domestic.asp?](http://www.kyochon.com/shop/domestic.asp?)
교촌치킨은 시/도, 구/군 별 Select 항목을 선택해야 해당 지역의 매장 결과가 출력되었습니다.
option값을 이용해 url을 변경, 요청을 반복하여 모든 매장을 탐색했습니다.
참고) 초기에 시/도의 select 태그 선택 후, 구/군의 option값들을 읽어들이는 방식을 선택했지만, Javascript가
완전히 로드되지 않은 상태로 html 읽어들여, 원하는 결과를 얻지 못했습니다. selenium 라이브러리를 사용하면, 비슷한 문제를 해결할 수 있습니다.