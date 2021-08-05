
#예외 고급
#try :
#except 예외의종류클래스 as 오류를담을 객체명 :

# 1. Exception : 예외클래스[ 최상위 예외클래스 ]
# 2. ValueError , IndexError 등 : 예외클래스
'''
리스트= [ ]
try :
    int(input("정수 입력 : "))
    print(리스트[2])
except ValueError as e :
    print("예외발생 사유 : " , e )
except IndexError as e :
    print("예외발생 사유 : " , e )
except Exception as e :
    print("예외발생 사유 : " , e )
'''

# 문제1
def signup() : # 함수 정의
    try :
        id = input("ID : ")
        password = input("password : ")
        name = input("name : ")
        phone = int( input("phone : ") )
    except ValueError as e :
        print(" 경고 : 회원가입 실패 [ 사유 : " , e , "] ")
    else :
        print(" 알림 : 회원가입 성공 ")
        return # 함수 종료
    finally:
        print(" 알림 : 회원가입 종료 ")

try :
    signup()  # 함수 호출
except Exception as e :
    print(" 경고 : 회원가입 실패 [ 사유 : " , e , "]  ")




