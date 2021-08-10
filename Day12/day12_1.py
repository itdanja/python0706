
# 파이썬 => 데이터 가공/다루기 =>
# CSV 파일 다루기

import csv  # csv 관련된 함수 제공

# 1. csv 파일 가져오기
file = open( "csv연습.csv" , "r") # 해당 파일 읽기 모드[r]
# 2. csv 파일 읽기 
contents = csv.reader(file) # csv.reader(파일객체) : 해당 파일의 내용을 줄당 1하나의리스트 => 2차원리스트 로 읽기
# 3. csv 출력
for i in contents :
    print( i )

# 4. csv 파일 쓰기
점수목록 = [ ["유재석","강호동","신동엽"] , [90,80,70] , [60,80,70] ]
file = open( "csv연습2.csv" , "w" ) # 해당 파일 쓰기 모드[w]
contents = csv.writer( file , delimiter =',' )   # 쓰기설정 [ delimiter : 요소들의 구분 기준 ]
contents.writerows( 점수목록 ) # 쓰기
####################################################################
# 활용1
# 행정안전부 홈페이지 => 정책자료 => 통계
전국인구파일 = open("201912_202107_주민등록인구및세대현황_월간.csv","r")
통계리스트=csv.reader(전국인구파일) #읽기
for i in 통계리스트 :
    #print( i[0] ) #행정구역 이름
    print(i[0].split(" ")[0], ":", end=" ")
                                 # 마지막에 공백처리
    for index in range( 1 , 20 , 6) :
        print( i[index] , end=" " )
    print( )
# 활용2
# 국토교통부 실거래가 공개시스템 => 실거래가 자료제공
서울아파트파일 = open("아파트(매매)__실거래가_20210810194808.csv" , "r")
통계리스트 = csv.reader(서울아파트파일) # 파일읽기
통계 = [ ]
for i in 통계리스트 :
    통계.append( i )
print( 통계[16][0] , " : " , 통계[16][4] , 통계[16][8] , "만원"  )
        # 2차원[행][열]