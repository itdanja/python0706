
# 변수 [ 메모리 = 자원 ]
    # 파이썬은 자료형[메모리크기] 자동할당
#c,java
    #int 변수명 = 10
# python
변수명 = 10
print( type(변수명) )
# 연산자
    # 산술연산자
    # 논리연산자
    # 비교연산자
    # 대입연산자
    # 대입연산자

# 문제1 : 급여 명세서
    # 조건 : 기본급 , 수당 입력받아 변수에 저장
    # 출력 : 실수령액 [ 실수령액 계산방식 : 기본급 + 수당 - 세금[ 기본급 10% ]
    # 출력 예 : 실수령액 ~~~ 입니다

기본급 = int( input("기본급 입력 : ") ) # input 기본 타입은 문자
수당 = int( input("수당 입력 : "))
실수령액 = 기본급 + 수당 - (기본급*0.1)
    # 100% : 1      10% : 0.1    1% : 0.01      50% : 0.5
print( " 실수령액은 : " , 실수령액 )

# 문제2 : 지폐 세기
    # 조건 : 금액 입력받아 입력받은 금액의 지폐수 세기
    # 입력 예 : 356789
        # 출력
        # [ 예 ] : 356789 =>
        #              * 			십만원 : 3장
        #              * 			만원 : 5장
        #              * 			천원 : 6장
        #              * 			백원 : 7개

# 문제3 :반지름을 입력받아 원 넓이 출력하기
반지름 = int( input( "원의 반지름 입력 : " ) ) # int( 값 ) => 정수
원넓이 = 반지름 * 반지름 * 3.14
print(" 입력받은 반지름의 원 넓이는 : " , 원넓이 )

# 문제4 :
실수1 = float( input( " 실수1 입력 : " ) )    # float( 값 ) => 실수
실수2 = float( input( " 실수2 입력 : " ) )
결과 = (실수1/실수2) *100
print( "결과는 : " , 결과 , "%" )
# print(  실수1/실수2 ) # 나누기
# print( 실수1//실수2 ) # 나누기 후의 몫

# 문제5 :
윗변 = int( input("윗변 입력 : ") )
밑변 = int( input("밑변 입력 : ") )
높이 = int( input("높이 입력 : ") )
사다리꼴 = ( 윗변 * 밑변 ) * 높이 / 2
print(" 사리꼴의 계산 후 : " , 사다리꼴 )

# 문제6 :
키 = int( input(" 키 입력 : "))
표준체중 = ( 키-100 ) * 0.9
print("해당키의 표준체중 : " , 표준체중 )

# alt + shift + e   : 한줄씩 컴파일후 결과

'''
    문제7 : 키와 몸무게를 입력받아 BMI 출력하기
        BMI 계산식 = > 몸무게 / ((키 / 100) * (키 / 100))
    
    문제8 :  inch 를 입력받아 cm 로 변환하기
    
    문제9 :중간고사, 기말고사, 수행평가를 입력받아 반영비율별 계산하여
        //소수 둘째 자리 까지 점수 출력하기
        //	// 중간고사 반영비율 => 30 %
        //	// 기말고사 반영비율 => 30 %
        //	// 수행평가 반영비율 => 40 %
    
    예제10: 연산 순서 나열 하고 x와 y값 예측하기
        //int x = 10;
        //int y = x-- + 5 + --x;
        //printf(" x의 값 : %d , y의값 :  %d ", x, y)
'''














