# 반복문 [ for , while ]
    # for 변수 in range( 숫자 )
        # 0부터 숫자 전까지 1씩 증가하면서 변수에 대입 하면서 반복
    # for 변수 in range( 시작번호  , 끝번호 )
    # for 변수 in range( 시작번호  , 끝번호 , 증감 )
    # for 변수 in [ 값1 , 값2 , 값3 ~~~ ]
        # 값1 ~ 값3 하나씩 변수에 대입 하면서 반복
    # for 중첩
        # for i in range( 1 , 3 ) :
            # for j in range( 4 , 6 ) :
                # print(  i , j )
                        # i 가  1일때  j = 4 , 5
                        # i 가  2일때  j = 4 , 5
'''
#예1
for x in range(3) :
    print( x , "번 실행중")
for x in [ 1 , 2 ,3 ] :
    print( x , "번 실행중 ")
for x in ["a" , "b" , "c"] :
    print( x , "실행중 ")
###########################################
#예2
for x in range( 1 , 3 ) :
    print( x , "번 실행중")
for x in range( 1 , 11 , 2 ) :
    print( x , "번 실행중")
##############################################
#예3 : 1부터 10까지 출력
for x in range( 1 , 11 ) :
    # print( x )  # print() 출력후 줄바꿈처리 [자동]
    print( x , end=" " )    # ,end=출력후 처리문

print()
# : 1부터 100까지 7의 배수 출력
for x in range( 1 , 101 ) :
    # 7의배수
    if x % 7 == 0 :
        print( x , end=" ")
print()
# 1부터 100까지 7의 배수 이면서 홀수만 출력
for x in range( 1 , 101 ) :
    if x % 7 == 0 and x % 2 == 1 :
        print( x , end=" ")
print()
# 1부터 100까지 누적합계
누적합계 = 0
for x in range( 1 , 101 ) :
    누적합계 += x
print(" 1~100까지 총누적합 : " , 누적합계 )
# 1부터 100까지 3의 배수만 누적합계
누적합계 = 0
for x in range( 0 , 101 , 3 ) :
    누적합계 += x
print(" 1~100까지 3배수의 총누적합 : " , 누적합계 )
#
누적합계 = 0
for x in range( 1 , 101 ) :
    if x % 3 == 0 :
        누적합계 += x
print(" 1~100까지 3배수의 총누적합 : " , 누적합계 )
'''
'''
#문제1. 2단의 구구단 출력
print("---------2단")
for 곱 in range( 1 , 10 ) :
    print( "2 X" ,곱 ,"=" , (2*곱) )

#문제2  2~15단까지 구구단 출력
    # 2단=> 9번실행     3단=> 9번실행
        # 단 마다 9번씩 곱 반복
for 단 in range( 2 , 16 ) :
    print("---> " , 단 , "단---->")
    for 곱 in range( 1 , 10 ) :
        print( 단 , "X" , 곱 , "=" ,(단*곱) )

# 별찍기 예제1  : 입력한 정수만큼 별 출력
별 = int( input("별 개수 : "))
for s in range( 1 , 별+1 ) :
    print("★" , end=" ") # ㅁ+한자키 : 특수문자

print()
# 별찍기 예제2  : 입력한 정수만큼 별 출력 [ 5개마다 줄바꿈 ]
별 = int( input("별 개수 : "))
for s in range( 1 , 별+1 ) :
    print("★" , end=" ")
    if s % 5 == 0 : print()
        # 별이 5의 배수이면 줄바꿈
'''

#별찍기1 :
'''         i = 현재줄     s = 별 
	*       i=1         s = 1 
	**      i=2         s = 1 2 
	***     i=3         s = 1 2 3
	****    i=4         s = 1 2 3 4
	*****   i=5         s = 1 2 3 4 5
	공식    i는1씩증가    s는 1부터 i까지 
'''
줄 = int(input("줄수 : "))
for i in range( 1 , 줄+1 ) :
    for s in range( 1 , i+1 ) :
        print("★" , end="")
    print() # i 마다 줄바꿈





