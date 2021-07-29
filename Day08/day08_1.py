
# 함수 :
# 함수 형태
# def 함수이름( 인수1 , 인수2 , 인수3 ~~ )
#     여러가지 코드
#     return 반환데이터

# 재귀함수 : 현 함수를 재 호출

n = int( input("팩토리얼 수 : ") )
# 함수 없는 팩토리얼
fact = 1
for i in range( 1 , n+1 ) :
    # i는 1부터 입력한값까지 1씩증가하면서 i에 대입반복
    fact = fact * i     # fact *= i
    # 대입연산자
print( "입력한 수의 ![팩토리얼] 값은 " , fact )

# 재귀함수를 이용한 팩토리얼
def 팩토리얼함수( n ) :
    if n == 1 : # 1의 팩토리얼은 1
        return 1
    else:
        return n * 팩토리얼함수(n-1)

n = int( input("팩토리얼 수 "))
f = 팩토리얼함수( n )
print( "입력한 수의 ![팩토리얼] 값은 " , f )

#순서도
    # n : 3 일때      return 3 * 재귀함수(2)       return 3 * 2
        # n = 2     return 2 * 재귀함수(1)        return 2 * 1
        # n = 1     return 1            -------

    # n : 5 일때      return 5 * 재귀함수(4)     return 5 * 24        ===> 최종 리턴 = 120
        # n = 4     return 4 * 재귀함수(3)      return 4 * 6
        # n = 3     return 3 * 재귀함수(2)      return 3 * 2
        # n = 2     return 2 * 재귀함수(1)      return 2 * 1
        # n = 1     return 1                 -------------

# 터틀이용한 재귀 활용
import turtle # 터틀 관련된 메소드 제공

def tree( length ) : # 나무 그리는 함수
    if length > 5 :  # 길이가 5 미만이면 함수 종료
        t.forward(length) # 길이만큼 전진
        t.right( 20 ) # 오른쪽으로 20도 회전
        tree( length-15 )  # 재귀 90 - 15 - 15 -15 -15  -15
        t.left(40)
        tree( length - 15 ) # 재귀 90 -15 -15 -15 -15 -15
        t.right(20)
        t.backward( length )

t = turtle.Turtle("turtle")
t.left(90) # 거북이 왼쪽 90도 회전

t.color("green") # 거북이 색상
t.speed(0) # 거북이 속도

tree( 90 )  # 함수 호출 = 인수는 90

turtle.mainloop() # 터틀 계속 보이기


'''
# 순서도
    # 길이 = 60  오른쪽 20    [재귀]45     오른쪽20 [재귀]30    오른쪽20[재귀]15     오른쪽20[재귀]0  return
                                                                                왼쪽40 [재귀]0
                                                            왼쪽40 [재귀]15     오른쪽20 [재귀]0
                                                                                왼쪽40 [재귀]0
                                        왼쪽40 [재귀]30     오른쪽20[재귀]15     오른쪽20[재귀] 0 
                                                                                왼쪽40[재귀] 0
                                                            왼쪽40 [재귀]15     오른쪽20 [재귀] 0                                                                           왼쪽40[재귀] 0
'''










