
# HTML : 웹문서 : 하이퍼텍스트 마크업 언어
    # 마크업   <명령어>
    # import csv :  csv 관련 메소드
import urllib.request as ur             # url 관련된 요청 함수 모듈
from bs4 import BeautifulSoup as bs     # html에서 데이터 추출 관련 함수 모듈

#예1) 웹사이트[페이지] HTML
url = "http://quotes.toscrape.com" #1.주소 입력
html = ur.urlopen( url )            #2. 해당주소를 파이썬으로 가져오기

soup = bs( html.read() , "html.parser") #3. 해당 페이지의 데이터 가져오기

# 1.
# <span> : html의 특정 상자구역
#print( soup.find_all("span") )
    # soup.find_all("태그명")  : 해당 태그명 검색
# 2.
# <div> : html의 특정 상자구역
#print( soup.find_all( "div" , {"class":"quote"} )[0] )
    # soup.find_all("태그명") : 해당 태그명 검색 => 해당 태그의 클래스의 이름이 quote 검색

# 3.
#for i in soup.find_all( "div" , {"class":"quote"} ) :
#    print( i )

#예2 )  네이버영화에서 현재 상영중인인 영화
url = "https://movie.naver.com/movie/running/current.naver"  # 주소 넣기
html = ur.urlopen(url) # 주소 열기

soup = bs(html.read() , "html.parser") # 해당 주소에서 데이터 가져오기
# <ul> : html의 순서목록
ul = soup.find_all( "ul" , {"class":"current_list"} ) # 데이터중에 검색 [ ul 태그에 class 이름이  current_list ]
print( ul )

#예3 ) 네이버영화에서 현재 상영예정인 영화
url = "https://movie.naver.com/movie/running/premovie.naver"
html = ur.urlopen(url)

soup = bs(html.read() , "html.parser")
ul = soup.find_all( "dt" , {"class":"tit"})
print( ul )

for i in soup.find("dt" , class_="tit").find_all( "a" ):
    print( i.get("href") )



from bs4 import BeautifulSoup as bs
import os , re  # os = 시스템 모듈  , re = 정규식 모듈
import urllib.request as ur  # URL 관련 요청 함수 모듈

url = 'https://news.daum.net/'          # 1. 주소 넣기
html = ur.urlopen(url)                  # 2 주소 열기
    # html : 하이퍼텍스트 마크업 언어 => 웹문서 [ 웹페이지 ]

soup = bs( html.read() , 'html.parser')

ul=soup.find_all( 'strong',{"class":"tit_g"})

for i in soup.find_all('a') :
    print( i.get('href') )


url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90"

html = ur.urlopen(url)                  # 2 주소 열기
    # html : 하이퍼텍스트 마크업 언어 => 웹문서 [ 웹페이지 ]

soup = bs( html.read() , 'html.parser')

ul=soup.find( 'span' ,class_="spt_con dw").text
print( ul )

