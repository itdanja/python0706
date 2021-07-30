

# 클래스 설계 [ 변수 , 메소드 ]
#1. 클래스 선언
class Member :
    def __init__(self , id , password , name , phone ):
        self.id = id
        self.password = password
        self.name = name
        self.phone = phone

    def memberinfo(self):
        print( self.id , self.name , self.name , self.phone )

memberlist = [ ]

while True :
    print(" [[[[ 회원제 관리 프로그램 ]]]] ")
    print("1.회원가입 2.로그인 3.종료")
    ch = int(input("선택 : "))
    if ch == 1 :
        id = input("아이디 : ")
        password = input("비밀번호 : ")
        name = input("이름 : ")
        phone = input("연락처 : ")
        temp = Member( id , password , name , phone )
        print("회원[객체] 가입 완료 ")
        memberlist.append( temp )
    if ch == 2 :
        id = input("아이디 : ")
        password = input("비밀번호 : ")
        for i in memberlist :
            if i.id == id :
                if i.password == password :
                    print( " 로그인 성공 ")
                    for j in memberlist :
                        j.memberinfo()
                    break


