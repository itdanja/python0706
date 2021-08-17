

# API 클라이언트 정보
import json # json 라이브러리
import re # 정규표현식 라이브러리
import urllib.parse
import urllib.request

client_id = "w9HPzgkd7qUCVergunhj"      #신청한 클라이언트의 아이디
client_secret = "ltRrRXkmKV"            #신청한 클라이언트의 비밀번호

# 도서검색 URL
url = "https://openapi.naver.com/v1/search/book.json"
# 옵션 [ 표시할 결과수 , 정렬기준( count=판매순) ]
option = "&display=10&sort=count"
# 조건
query = "?query=" + urllib.parse.quote( input("도서검색: ") )
# RUL+조건+옵션
url_query = url + query + option

# api 검색 요청 개체 설정
request = urllib.request.Request( url_query )
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

# 검색 요청
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
else:
    print("Error Code:" + rescode)

텍스트 = response_body.decode("utf-8")
json텍스트 = json.loads(텍스트) # 해당 텍스트를 json으로 호출 [ 쌍 = 키:값 ] => 딕셔너리
    # json 언어   키(속성):값  이루어진 한쌍
print( json텍스트 )    # 딕셔너리{ 키 : 리스트[{ 키:값} ]
# items 속성 불러오기
for i in json텍스트['items'] :
    # 정규표현식 => 패턴찾기
    타이틀 = re.sub( "<.+?>" , "" , i["title"] )
        # re : 정규표현식
            # sub : 정규표현식에서 사용되는 치환 함수
                # sub( "패턴" ,새로운문자 , 대상 )
                    # <.+?> : 패턴을 공백으로 치환 .+?
                    # < 시작하고 한글자 이상이 있으면 그 뒤에 > 끝나는 패턴
                    # .+? 한글자 이상
    print( 타이틀 )

