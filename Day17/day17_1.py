
# 자료구조 : 자료의 조직, 관리, 저장을 의미한다 [데이터 값의 모임]

# 스택 : 스택은 한 쪽 끝에서만 자료를 넣거나 뺄 수 있는 선형 구조
    # 1. 입출구 가 동일
    # 2. 프링글스 과자통 , 컵홀더 , ctrl+z[ 명령 취소 ]등
    # 3. LIFO 후입선출

# 파이썬으로 스택 구현1
stack = [ None , None , None , None , None ] # None 공백
top = -1    # 가장 위에 데이터 위치 기억

top += 1            # 한칸 올라가기
stack[top] = "커피" # 커피 넣기
top += 1            # 한칸 올라가기
stack[top] ="녹차"    # 녹차 넣기
top += 1            # 한칸 올라가기
stack[top] = "꿀물"   # 꿀물 넣기

print(" --------------------- 스택 상태 --------------------")
for i in range( len(stack)-1 , -1 , -1 ):
    print( stack[i] )

print(" ---------------------- pop : 데이터 추출 ------------- ")

data = stack[top]   # 가장 위에 있는 데이터 => 꿀물
stack[top] = None   # 가장 위에 있는 데이터를 공백으로 변경
top -= 1            # 한칸 내려가기
print( " pop -> " , data )  # pop 데이터 확인

data = stack[top]
stack[top] = None
top -= 1
print( " pop -> " , data )

data = stack[top]
stack[top] = None
top -= 1
print( " pop -> " , data )

print(" --------------------- 스택 상태 --------------------")
for i in range( len(stack)-1 , -1 , -1 ):
    print( stack[i] )



