
# 예외처리 : 오류 발생
    # 목적 : 프로그램 실행시 오류발생--> 프로그램 다운
        # 오류발생시 -> 해당 코드의 대체코드 [ 프로그램의 정상화 ]
    # try : 예외발생 예상코드
    # except : 예외발생 했을경우 코드
    # else :    예외발생 없을경우 코드
    # finally : 무조건 실행되는 코드
    # 예외처리 클래스
        # Exception 클래스
            # Exception as 객체명 : 오류난 메시지 객체에 담기
# 예제1 :
#print("#프로그램시작!")
#    print("#프로그램시작!") # 코드상 오타 오류 발생

# 예제2 :
#print( input("숫자입력:")  >= 5  ) # 문자 입력시 타입 오류 발생

# 예제3 :
#list = [ ]
#print( list[1] ) # 메모리 부족하거나 없을경우 오류 발생

# 예외처리1
# try :   # : 콜론
#     print( input("숫자입력:") >=5 ) # 예외발생!!!!! ----> except 으로 이동
#     print("[[강제 오류]]")
# except :
#     print("[[오류발생]]")

# 예외처리 문법
#try :
    # 예외[오류] 발생할 가능성이 있는 코드
#except :
    # 예외 발생시 코드

# 예외처리2 : pass
'''
리스트 = [ ]
for i in range(5) :
    try :
        숫자 = int(input("리스트에 담을 숫자 : "))
        float(숫자)   # int형 ---> float 형    정수 ----> 실수 변환
        리스트.append( 숫자 ) # .append() : 리스트 요소 추가
    except :
        pass # 다음으로 이동
print( 리스트 )
'''

# 예외처리3 : else
'''
try :   # 1. 예외 발생할것 같은 코드
    숫자 = int(input("리스트에 담을 숫자 : ") )
    float(숫자)
except : # 2. try에서 예외 발생시 실행코드
    print(" 숫자 입력해주세요 ")
else :  # 3. try에서 예외 발생 안했을경우 실행코드
    print(" 정상적으로 입력했습니다 ")
'''
# 예외처리4 : finally
'''
try :
    숫자 = int( input("숫자 입력 : "))
except : # 1. 예외가 있을경우
    print("문자 입력 안됩니다!")
else:   # 2. 예외가 없을경우
    print("정상 입력 했습니다!")
finally:    # 3. 예외가 있든 없든 실행 [ 무조건 실행 ]
    print("프로그램 종료 ")
'''
# 예외활용1 : 반복문 예외
'''
while True :
    print("1.로그인 2.회원가입 3.종료 ")
    try:
        ch = int(input("번호 선택 : "))
        if ch == 1 :
            print(" 로그인 실행 ")
        if ch == 2 :
            print(" 회원가입 실행 ")
        if ch == 3 :
            print(" 프로그램 종료 ")
            break
        if ch < 1 or ch > 3 :
            print(" 없는 번호 입니다 ")
    except :
        print(" 문자 입력 불가능입니다 ")
'''
# 예외활용2 : 파일 예외
try :
    file = open("info.txt" , "r" ) # 파일 쓰기 [ w:쓰기 r:읽기 a:이어쓰기 ]
except Exception as e : # 예외클래스 as 객체명 : 오류난 내용[메시지] 예외객체 담기
    print(" 예외발생 사유 : " , e)






