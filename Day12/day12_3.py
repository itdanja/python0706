

# 활용4
# 한국거래소 => 정보데이터시스템 => 종목 카카오 시세
import csv
# 1. csv 파일 가져오기
from itertools import count

카카오시세파일 = open( "data_0127_20210810.csv" , "r")
카카오종목 = csv.reader( 카카오시세파일 )
# 2. 리스트에 담기
시세 = [ ]
for i in 카카오종목 :
    시세.append(i)
시세.pop(0)
# 3. 1년간 가장 높은 종가의 일자 출력
max = 0
for i in 시세 :
    if max < float(i[1]) :
        max = float(i[1])
        date = i[0]
print(" 카카오 가장 높은 시세 : " , max , date )
# 4. 대비가 증가했을때 평균(거래량) 대비가 감소했을때 평균(거래량) 출력
증가리스트 = [ ]
감소리스트 = [ ]
for i in 시세 :
    if float(i[2]) > 0 :
        증가리스트.append( i )
    elif float(i[2]) < 0 :
        감소리스트.append( i )
sum = 0
count = 0
for i in 증가리스트 :
    sum += float(i[7])
    count += 1
print( "전달 대비 증가 했을때 거래량 : " , sum/count)

sum = 0
count = 0
for i in 감소리스트 :
    sum += float(i[7])
    count += 1
print( "전달 대비 감소 했을때 거래량 : " , sum/count)