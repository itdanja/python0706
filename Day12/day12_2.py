
# 활용3
import csv
import re

부동산파일 = open( "아파트(매매)__실거래가_20210810194808.csv" , "r"  )
부동산통계 = csv.reader( 부동산파일 )
아파트 = [ ]
for i in 부동산통계 :
    아파트.append( i )

# 문제1 : 서울지역에 아파트의 면적이 120 이상 이면서 실거래가 20억이하 검색
import re # 정규 표현식

def switch(아파트) : # 문자열 => 숫자열 함수
    for i in 아파트 :
        for j in i :
            try :
                i[i.index(j)] = float( re.sub(',','', j ) )
                                        #re.sub() : 문자열 치환[교환]
                                        #re.sub("정규표현식","대상문자열","치환문자")
            except :
                pass
    return 아파트
switch(아파트)
서치리스트 = [ ]
for i in 아파트 :
    # str => float(실수형) 변환
    try:
        if i[5] >= 120 and i[8]<=200000 :
            print( "단지명 : " , i[4] , "   실거래가 : " , i[8] )
            서치리스트.append( i ) # 찾은 리스트를 서치리스트에 담기
    except : pass
# 문제2 : 문제1 검색된 내용을 csv 파일로 저장 하기
f = open( "서울아파트의 면적이120이상이면서 실거래가 20억이하인 아파트목록.csv" , "w" , encoding="utf8")
저장 = csv.writer( f , delimiter = ',') # 구분 기호
저장.writerows(서치리스트) # writerows : 모든 행단위를 쓰기
