from urllib.request import Request, urlopen
from datetime import datetime
import sys

# 크롤러 모듈에서 제공하는 에러함수 사용
def error(e):
    print('%s : %s' % (e, datetime.now()), file=sys.stderr)



def crawling(
        url='',
        encoding='utf-8',
        err=error):
    try:
        request = Request(url)
        response = urlopen(request)
        try:
            receive = response.read()
            # 인코딩 방식이 다양하면 어떻게 해야할까 ?
            result = receive.decode(encoding)
        except UnicodeDecodeError:
            # Legal values for this argument are
            # 'strict' (raise a UnicodeDecodeError exception),
            # 'replace' (use U+FFFD, REPLACEMENT CHARACTER),
            # 'ignore' (just leave the character out of the Unicode result), or
            # 'backslashreplace' (inserts a \xNN escape sequence)
            result = receive.decode(encoding, 'replace')
        return result
    except Exception as e:
        err(e)