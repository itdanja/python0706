
# 문제
# 메모장 파일의 텍스트를 반대로 출력하는 스택 구현

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
SIZE = 1000
stack = [ None for _ in range(SIZE) ] # 스택[리스트]에  입력받은 크기만큼 None 할당
top = -1 # 초기 위치

file =  open("애국가.txt" , "r" , encoding="UTF8")
stack = file.readlines()

print("------- 원본 -------")
for line in stack :
    # 스택에 각 라인 push
    push(line) # 읽어온 한 줄씩 push
    print( line , end='')
print()
print("------- 각 줄 거꾸로 출력 -------- ")
while True :
    line = pop() # 한줄 추출
    if line == None : # 추출이 없으면
        break # 무한루프 종료

    ministack = [ None for _ in range( len(line) ) ]  # 추출한 문자열내 문자수 만큼 스택 리스트 선언
    minitop = -1

    for ch in line : # 문자열에서 단어 하나씩
        minitop += 1    # top 한칸씩 올리면서
        ministack[minitop] = ch # 단어 넣기

    while True :
        if minitop == -1 : # 단어가 없을때 까지
            break
        ch = ministack[minitop]
        minitop -= 1
        print( ch , end="")






