

# 프로젝트 생성
    # 디렉토리 생성 [폴더]
        # 파이썬 파일 생성

# 파이썬 작성시 주의점
#   1. 주석처리
#   2. tab[들여쓰기]
#   3. 명령어/함수 자동완성

# Day01
    # 1.출력  print() 함수
print(2)        #숫자 출력
print(2+3)      # 숫자 + 숫자
print("컴퓨터")  # 문자출력
print(2*3)      # 숫자 연산
print(2/3)      # 숫자 연산
print(3-2)      # 숫자 연산
print('컴퓨터')    # 문자출력
#print(컴퓨터)      # 문자입력시 키워드를 제외한 모든 문자처리
                    # 키워드 : 미리 정의된 단어
print("컴퓨터" + "마우스" )   # 문자 + 문자 => + 연결연산자
print("컴퓨터" * 10 )          # 문자 * 10 => * 문자반복횟수
# print("컴퓨터" / 10 )
# print("컴퓨터" - 10 )

# 라이브러리 [ 미리 만들어진 함수들의 집합 ]
    # import : 가져오기
import turtle   # turtle 라이브러리 가져오기

t = turtle.Turtle() # = 대입 [ 오른쪽데이터가 왼쪽데이터 이동 ]

t.shape("turtle")   # t의 모양
t.forward(100)      # 전진
t.left(90)          # 왼쪽 회전
t.forward(100)      # 전진
t.left(90)          # 왼쪽 회전
t.forward(100)      # 전진
t.left(90)          # 왼쪽 회전
t.forward(100)      # 전진

# 인덱스 [ ] : 색인 : 특정기준에 따른 나열 [ 0번시작 ~ ]
print("안녕하세요"[0] ) # 첫번째 글자 출력
print("안녕하세요"[1] )  # 두번째 글자 출력
print("안녕하세요"[2] )  # 세번째 글자 출력

print("안녕하세요"[-0])  # 첫번째 글자 출력
print("안녕하세요"[-1])  # 마지막글자부터 # 마지막글자
print("안녕하세요"[-2])  # 뒤에서부터 두번째글자

# 슬라이싱 [  :  ]  : 범위 색인 ~
print("안녕하세요"[0:2] )       # 0 ~ 1
print("안녕하세요"[1:3] )        # 1 ~ 2
print("안녕하세요"[2: ] )        # 2부터 끝까지

# 문자 길이 = len("문자")
print( len("안녕하세요") )



















