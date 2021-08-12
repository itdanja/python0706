# 문제 1: 네이버에서 날씨를 검색하여 현재날씨의 온도를 파이썬에서 출력
import urllib.parse
import urllib.request as ur
from bs4 import BeautifulSoup as bs

지역 = input(" 날씨 정보 지역명 ")
지역날씨 = urllib.parse.quote( 지역 + "날씨")  #  urllib.parse.quote( 문자 ) : 문자를 주소형식 변환
주소 = "https://search.naver.com/search.naver?&query=" + 지역날씨
    # 한글은 컴퓨터 바로 인식불가  : utf8 [ 한글인코딩 ]

html = ur.urlopen( 주소 )
soup = bs( html.read() , "html.parser")

날씨 = soup.find("span" , class_="todaytemp").text
print( " 현재 날씨 :  " + 날씨 + " 도 입니다" )
# # 미세먼지
# print( " 미세 먼지 : " + soup.find("dd",class_="lv1").text + " 입니다 " )
# #print( " 초미세 먼지 : " + soup.find_all("dd",{"class":"lv1"} )[1] + " 입니다 " )

for i in soup.find_all("dd",{"class":"lv2"}) :
    print( i.text )

# # 오존 지수
# print( " 오존 지수 : " + soup.find("dd",class_="lv2").text + " 입니다 " )




