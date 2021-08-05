


# 코드 오류 발생시  : 다른 코드 대체
    # 오류 종류 : 1. 코드상 오타

# # 예외발생1
# print("#프로그램 시작!")
#     #print("# 강제 오류 발생 ) : 코드상 오타 오류 발생
#
# # 예외발생2
# print( int( input("숫자입력:") ) >= 5 ) #  문자 입력시 타입 오류 발생
#
# # 예외발생3
# print(  list[1] ) # 메모리가 없을경우 오류 발생

# 예외처리 1
# try :  # 예외 묶어주기 : try 안에서 오류 발생시 except 으로 이동
#     print( int(input("숫자입력:") ) >=5 )
#
#     #print("강제 오류 )
#     print( list[1] )
#
# except: # try 에서 오류 발생시 코드 실행
#     print("오류 발생")

# 예외처리 문법
# try :
#     예외 발생할 가능성이 있는 코드
# except :
#     예외 발생시 코드

# 예외처리2 : pass
# 리스트 = [ ]
# for i in range(5):
#     try:
#
#         숫자=int(input("리스트에 담을 숫자 : "))
#         float(숫자)
#         리스트.append( 숫자 )
#
#     except :
#         pass
#
# print( 리스트 )

#예외처리3 : else:
# try : # 오류발생시 except 이동
#         # 오류 없을경우  try 코드 실행후 => else 이동
#     숫자=int(input("리스트에 담을 숫자 : "))
# except :
#     print(" 숫자 입력해주세요 ")
# else:
#     print(" 숫자를 정상적으로 입력했습니다")

#예외처리4 : finally
# try : # 예외 가능성 있는 코드
#     int( input("숫자입력:"))
# except : # 예외 발생시 코드
#     print(" 문자 입력 안됩니다 ")
# else: # 예외 발생 없을경우 코드
#     print(" 정상 작동 ")
# finally: # 무조건 실행되는 코드
#     print(" 프로그램 종료 finally ")

# #예제1 : 반복문 , 예외
# while True :
#     print("1.로그인 2.회원가입 3.종료")
#     try:
#         선택 = int( input(" 번호선택 : ") )
#         if 선택 == 1 :
#             print(" 로그인 실행 ")
#         if 선택 == 2 :
#             print(" 회원가입 실행 ")
#         if 선택 == 3 :
#             print(" 프로그램 종료 ")
#             break
#         if 선택 < 1 or 선택 > 3 :
#             print(" 알수 없는 번호 입니다")
#     except :
#         print(" 잘못 입력 하셨습니다 ")
#
# #예제2 : 파일 , 예외
# try :
#     file = open( "info.txt" , "w") # 파일 열기
# except Exception as e :
#     print( e ) # Exception : 예외처리 클래스 => 오류난 내용[메시지] 객체 로 담기
# finally:
#     file.close( )  # 파일 닫기
# print( file.closed )
#
# #예제3 : 함수 , 예외
#
# def 테스트() :
#     print(" 함수의 첫번째 줄 ")
#     try:
#         print(" 함수의 두번째 줄 ")
#         return #반환 : 함수 끝내기
#         print(" 함수의 세번째 줄 ")
#     except :
#         print( " except 실행 ")
#     else:
#         print( "else 실행 ")
#     finally:
#         print( "finally 실행")
#     print("함수의 마지막 줄 ")
#
# 테스트() # 함수 호출


#예외고급 :
# try :
#
# except 예외의종류 as 오류를담을 객체명 :
#
# try :
#     int( input(" 정수 입력 : "))
# except Exception as 오류 :
#     print( type(오류) )
#     print( 오류 )
#
# # 예러가지 예외 발생시 : type
# try :
#     int(input(" 정수 입력 : "))
#     print( 리스트[2] )
# except ValueError : # ValueError 관련된 예외만 처리
#     print( "정수만 입력 ")
#
# except NameError : #  NameError 관련된 예외만 처리
#     print( "리스트 이름의 오류 " )

# 모든 예외 잡기 Exception : 예외처리 슈퍼클래스

# 회원가입 메소드 : 아이디[str] , 비밀번호[str] , 이름[str] , 전화번호[int] , 성별[str]
    # 예외처리 : 사용자가 잘못된 입력의 타입이 오류일 경우 => 처음부터 다시 입력 하기
    # try[입력받기] except[가입실패] else[가입성공] finally[무조건실행]

def signup() :
    a = 0
    while a == 0 :
        try :
            id =  input(" id : ")
            password = input( " password : ")
            name = input( " name : ")
            phone = int( input( " Phone : ") )
            sex =   input(" gender : ")
        except ValueError :
            print( " 알림 : 회원가입 실패 [ 사유 : 입력오류 ]")
        except Exception :
            print( " 알림 : 회원가입 실패 [ 관리자에게 문의 ]")
        else:
            print( " 알림 : 회원가입 성공 ")
            return
        finally:
            print( " 알림 : 회원가입 종료 ")
signup()


# enumerate : 메소드 사용
t = [ 1 , 5 , 7 , 33 , 39 , 52 ]

for p in enumerate(t) :
    print( p )


for p2 in t :
    print( p2 )







































