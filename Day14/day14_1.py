

'''
    API : Application Programming Interface
   네이버 API
   // 1. 네이버 로그인
   // 2. 네이버 개발자센터 : https://developers.naver.com/main/
   // 3. API 신청
'''

    #신청한 api 클라인언트 정보

import os
import sys
import urllib.request
client_id = "w9HPzgkd7qUCVergunhj"  #신청한 클라이언트의 아이디
client_secret = "ltRrRXkmKV"            #신청한 클라이언트의 비밀번호

검색어 = input("검색어 : ")

encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

