#특정페이지의 소스코드를 수집하는 소스

import requests
#특정 url에 접속하는 요청객체(request)
request=requests.get('http://www.dowellcomputer.com/main.jsp') #get방식으로 실행
#접속한 이후의 웹사이트 소스코드를 추출합니다.
html=request.text
print(html)
