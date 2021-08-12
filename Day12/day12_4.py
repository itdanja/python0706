
#문제1:
import csv

확진자파일 = open("서울시 코로나19 확진자 현황.csv" , "r" , encoding="utf-8") # latin_1, euc-kr, cp949 , utf-8
확진자 = csv.reader(확진자파일  )
확진자리스트 = [ ]
for i in 확진자 :
    확진자리스트.append(i)

# 지역 검색 // 날짜 입력
날짜 = input(" 확진 일 :" )
count = 0 # 지역 확진자수
지역 = input(" 지역명[구] : ")
for i in 확진자리스트 :
    if i[5] == 지역 and i[1] == 날짜 :
        count += 1
print(날짜, " " ,지역,"의 확진자수 : " , count ,"명")



