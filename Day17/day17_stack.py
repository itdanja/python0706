
# 파이썬으로 스택 구조 구현1
# 함수
    # 1. 스택 Full 여부 확인 함수
    # 2. 스택 Empty 여부 확인 함수
    # 3. 스택 push 데이터 삽입 함수
    # 4. 스택 pop 데이터 삭제 함수
    # 5. 스택 peek top 위치의 데이터 확인 함수

#1.
def isstackfull() :
    global SIZE , stack , top    # 전역변수
    if top >= SIZE -1 : # 현재 top 위치가 사이즈에 마지막 자리이면
        return True # 자리 없음
    else:
        return False # 자리 있음
#2.
def isstackempty() :
    global SIZE , stack , top
    if top == -1 :  # 현재 top 위치가 -1 이면
        return True # 스택이 모두 비어 있음
    else:
        return False
#3.
def push(data) : # data를 인수로 받아 스택에 저장하는 함수
    global SIZE , stack , top
    # 자리가 있을경우에만
    if isstackfull() :# 자리가 없으면
        print(" 스택이 다 찼습니다. ")
        return
    top += 1 # top 올리기
    stack[top] = data # 해당 위치에 데이터 넣기

#4.
def pop( ) : # 현재 top 위치에 데이터 공백으로 변경
    global SIZE , stack , top
    # 스택이 비어있지 않으면
    if isstackempty() :
        print(" 스택이 비어 있습니다 ")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1 # top 내리기
    return data

#5.
def peek() :
    global SIZE , stack , top
    if isstackempty() :
        print(" 스택이 비어 있습니다 ")
        return None
    return stack[top]       # top 위치에 데이터 반환

# 전역변수 선언
SIZE = int( input(" 스택 크기 입력: ") ) # 스택의 크기를 입력받아
stack = [ None for _ in range(SIZE) ] # 스택[리스트]에  입력받은 크기만큼 None 할당
top = -1 # 초기 위치

# 메뉴
select = input(" 삽입[I] / 추출[E] / 확인[V]  / 종료[X] 중 선택 : ")
while select !="x" and select !="X" :
    if select == "I" or select =="i" :
        data = input(" 입력할 데이터 : ")
        push(data)
        print( " 스택 상태 : " , stack )
    elif select =="E" or select =="e" :
        data = pop()
        print(" 추출된 데이터 : " , data)
        print(" 스택 상태 : " , stack )
    elif select =="V" or select =="v" :
        data = peek()
        print(" 확인된 데이터 : " , data )
        print(" 스택 상태 : " , stack )
    else:
        print(" 알수 없는 행동 ")

    select = input(" 삽입[I] / 추출[E] / 확인[V]  / 종료[X] 중 선택 : ")

print(" 스택 프로그램 종료 ")












