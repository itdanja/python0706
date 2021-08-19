
#문제3
# 1단계 : 주어진 식에서 연산자의 위치 찾기
def func_1(expression) :
    for index , value in enumerate(expression ) :
                        # enumerate : 인덱스 , 값
        if value == "+" or value =="-" or value == "*" : # 해당 값이 연산자이면
            return  index # 해당 값의 위치를 반환

# 2단계 : 연산자의 앞과 뒤에 있는 문자열을 각각 숫자로 변환합니다.
def func_2( expression , ex_index ) :
    numA = int( expression[  : ex_index ]) # 인덱싱을 이용한 문자열 출력
                    # 처음문자부터 연산자 전까지 출력
    numB = int( expression[ ex_index+1 : ] )
                    # 연산자 다음부터 끝까지 출력
    return numA , numB

# 3단계 : 주어진 연산자에 맞게 연산을 수행합니다.
def func_3( numA , numB , ex ) :
    if ex =="+" :
        return numA + numB
    elif ex == "-" :
        return numA - numB
    elif ex == "*" :
        return numA * numB

def solution(expression) :
    ex_index =  func_1( expression )
    numA , numB = func_2( expression , ex_index )
    result = func_3( numA , numB , expression[ex_index]  )
    return result

expression = "123+12"
result = solution( expression )
print(" 문제3 결과는 " , result )