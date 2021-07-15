# 컴퓨터[ 기계어 = 0,1 ]

# 제어문 :
    # 목적 : 경우의수에 따른 코드 제어
    #  if : ~만약에
        # 제어 대상
            # 1. 논리 [true 혹은 false ]
        # 주의 점
            # 1. tab[들여쓰기]
    # 형태 
        # if 논리 : [참=true경우]실행문
        # else : [거짓=false경우]실행문
        ##################
        # if 논리1 :
        # elif 논리2 :
        # elif 논리3 :
        # elif 논리4 :
        # else :
# 예1 : true인 경우
if 3>1 : print("3이 크다")

# 예2 : true 혹은 false 경우
if 3>5 : print("3이 크다2")
else : print("5가 크다2")

# 예3 : true의 경우가 다수일때
if 3> 5 : print("3이 크다1 ")
elif 3 > 4 : print("3이 크다2 ")
elif 3 > 3 : print("3이 크다3 ")
elif 3 > 2 : print("3이 크다4" )
else: print( "참이 없다 ")

# 예4 : 하나의 점수를 입력받아 80점 이상이면 합격출력 아니면 탈락
점수 = int( input("점수 입력 : "))
if 점수 >=80 : print("[참]:합격")
else: print("[거짓]:불합격")

# 예5 : 하나의 점수를 입력받아 90점이상 "A등급" 80점 이상 "B등급" 70점 이상이면 "C등급" 그외 탈락 
점수2 = int( input("점수 입력 : "))
if 점수2 >=90 : print("[참1] : A등급")
elif 점수2 >=80 : print("[참2] : B등급")
elif 점수2 >=70 : print("[참3] : C등급")
else : print("[거짓] : 탈락")

# 문제1 : 하나의 점수 와 성별 를 입력받아
점수3 = int( input("점수 입력 : ") )
성별  = input( "성별 입력 : ")

if 점수3 >=90 :
    if 성별 == "남" : print("A-1")
    else : print("A-2")
elif 점수3 >=80 :
    if 성별 == "남" : print("B-1")
    else:print("B-2")
elif 점수3 >=70 :
    if 성별 == "남" : print("C-1")
    else:print("C-2")
elif 점수3 >=60 :
    if 성별 == "남" : print("D-1")
    else:print("D-2")
else:print("탈락")

#문제2 :
정수1 = int(input("정수1 : "))
정수2 = int(input("정수2 : "))
if 정수1 > 정수2 : print("큰수 : ",정수1 )
elif 정수1 < 정수2 : print("큰수 : ",정수2)
else: print("같다")

#문제3 :
정수1 = int(input("정수1 : "))
정수2 = int(input("정수2 : "))
정수3 = int(input("정수3 : "))
if 정수1>정수2 and 정수1 > 정수3 :  print("큰수 : ",정수1 )
elif 정수2>정수1 and 정수2 > 정수3 :  print("큰수 : ",정수2 )
elif 정수3>정수1 and 정수3 > 정수2 :  print("큰수 : ",정수3 )
else: print("같다")

#문제4 :
정수1 = int(input("정수1 : "))
정수2 = int(input("정수2 : "))
정수3 = int(input("정수3 : "))
정수4 = int(input("정수4 : "))
큰값 = 정수1 # 큰값을 저장하는 변수에 첫번째 값을 넣기
if 큰값 < 정수2 : 큰값 = 정수2  # 만약에 큰값에 있는 값보다 두번재 값이 더크면 교체
if 큰값 < 정수3 : 큰값 = 정수3
if 큰값 < 정수4 : 큰값 = 정수4
print( "가장 큰수는 : " , 큰값 )
print( "가장 큰수는 : " , max( 정수1 , 정수2 , 정수3 , 정수4 ) )
# max( 값1 , 값2 , 값3 , 값 ~~ ) : 가장 큰값을 출력





