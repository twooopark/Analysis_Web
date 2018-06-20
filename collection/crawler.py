from urllib.request import Request, urlopen
from datetime import datetime
import sys

def crawling(
        url='',
        encoding='utf-8',
        err=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr),
        proc=lambda html: html, # 전달된 함수가 없으면, 그냥 넘어감
        store=lambda html: html):# lambda html: print("processing..."+html)):
    try:
        request = Request(url)
        response = urlopen(request)
        try:
            receive = response.read()
            # 인코딩 방식이 다양하면 어떻게 해야할까 ?
            result = store(proc(receive.decode(encoding)))
            # if proc is not None: -->  proc=lambda html: html, 를 함으로써 생략가능해짐
            #         result = proc(result)
            # if store is not None: --> 위와 마찬가지로 생략
            #         result = store(result)
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