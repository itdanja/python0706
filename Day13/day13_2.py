
import urllib.request as ur         # url관련 함수 제공
from bs4 import BeautifulSoup as bs #데이터 추출 함수 제공

url = "https://www.daum.net"        #1.주소 넣기
daum =  ur.urlopen(url)             #2. 해당 주소 열기
soup = bs( daum.read() , "html.parser" ) # 해당 주소의 데이터 가져오기

# 특정 태그의 클래스 가져오기
print( soup.find_all("div",{"class" : "cont_item"}))
print( soup.find_all("strong",{"class":"tit_item"}) )

# a태그 5개 [ a : 주소링크 링크태그 ]
print( soup.find_all("a")[0:5] )

# a태그 링크
for i in soup.find_all("a")[ 0 : 5 ] :
    print( i.get("href") )

# 특정 기사 본문 가져오기 [ p :문단태그 ]
기사 = "https://news.v.daum.net/v/20210812174721787"
soup = bs( ur.urlopen(기사).read() , "html.parser" )
for i in soup.find_all("p") :
    print( i.text )

# 위에서 가져온 기사 본문를 파일에 저장
파일 = open("다음기사.txt" , "w")
for i in soup.find_all("p") :
    파일.write( i.text+"\n")
파일.close()




