import urllib.request as ur         #1.html 가져오는 함수 제공
from bs4 import BeautifulSoup as bs #2.html 데이터 가져오는 함수 제공
import urllib.parse                 #3.url제공 [ url구성 함수 제공 ]

def 검색( 키워드 , 타입 ) :
    키워드검색 = urllib.parse.quote(키워드)
    if 타입 == 2 :
        키워드검색 = urllib.parse.quote(키워드+"날씨")
    주소 = "https://search.naver.com/search.naver?query="+키워드검색
    페이지 = ur.urlopen(주소)
    데이터 = bs( 페이지.read() , "html.parser" )
    if 타입 == 1 : # 종목 검색
        try :
            현재가 = 데이터.find( "span" , class_="spt_con dw" ).text
            if "지수" in 현재가 :
                print(" 종목의 현재가[▼] : ", 현재가)
            else:
                현재가 = 데이터.find("span", class_="spt_con up").text
                print(" 종목의 현재가[▲] : ", 현재가)
        except :
            print(" 알수없는 종목명 입니다 ")
    if 타입 == 2 :
        print(" 현재 키워드 의 온도 : " , 데이터.find( "span" , class_="todaytemp").text )
        for i in 데이터.find_all("dd" , {"class":"lv2"} ) :
            print( i.text )
while True :
    선택 = int( input("1.주식 2.날씨 3.쇼핑 ") )
    if 선택 == 1 :
        키워드 = input(" 주식 종목명 입력 : ")
        검색( 키워드 , 1  )
    if 선택 == 2 :
        키워드 = input(" 지역명 : ")
        검색( 키워드 , 2  )




