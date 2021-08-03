
# 클래스 : 설계도[ 필드 , 함수 등 ]
# 객체 : 설계도 기반으로 만들어진 메모리
# 파일처리 : 보조기억장치 저장

# 회원클래스 설계
class Member :
    # 변수 [ 필드 ]
    # 인스턴스 함수 [ 객체생성시 초기값 ]
    def __init__(self , id , password , name , phone ):
        self.id = id
        self.password = password
        self.name = name
        self.phone = phone
    # 로그인 함수 [ 메소드 ]
    def login(self , id , password ):
        if self.id == id and self.password == password :
            print("[[ 로그인 성공 ]]")
    # 필드 저장
    def membersave(self) :
        file = open("memberlist.txt" , "a") # w  : 파일쓰기: r: 읽기 a:이어쓰기
        # 객체내 필드 구분하기 위한 , 기호
        # 객체 [ 회원구분 ]  \n : 줄바꿈
        file.write( self.id +","+self.password+","+self.name+","+self.phone+"\n")
        file.close()

memberlist = [ ]

while True :
    # 파일 불러오기
    file = open("memberlist.txt" , "r")
    m = file.read() # 모든 텍스트 읽어오기
    mm = m.split("\n") # 회원별 분리
    for i in mm :
        if not i : break # 만약에 회원이 null이면 끝내기
        # 각 회원 필드 분해
        mmm = i.split(",")
        memberlist.append( Member(mmm[0] , mmm[1] , mmm[2] , mmm[3]) )

    print( "----- 메인 페이지 ------- ")
    ch = int(input(" 1.회원가입  2.로그인"))
    if ch == 1 :
        id = input("아이디 : ")
        password =  input("비밀번호 : ")
        name =  input("이름 : ")
        phone = input("전화번호 : ")
        # 객체 생성과 객체를 리스트에 담기
            # 회원가입 중복체크 ~
        temp =  Member(id,password,name,phone)
        memberlist.append( temp )
        temp.membersave()

    if ch == 2 :
        id = input("아이디 : ")
        password = input("비밀번호 : ")
        for i in memberlist :
            i.login( id , password )












