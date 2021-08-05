# 주소록[객체] 프로그램 [ 파일처리 ]
    # [조건1] 모든 경우에도 프로그램 종료 X

class Contact : # 클래스 선언
    # 객체 초기값 : 객체 선언시 기본값[변수]
    def __init__(self , name , phone_number , e_mail , address ):
        self.name = name
        # self.name : 클래스[객체내] 의 변수
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.address = address
        # 클래스 밖에서 인스턴스 메소드로 들어온 인수[변수]
    # 객체 정보 출력
    def print_info(self):
        print(" Name : " , self.name )
        print(" phone_number : ", self.phone_number)
        print(" e_mail : ", self.e_mail)
        print(" address : ", self.address)

# 함수 [ 메뉴함수 , 등록 함수 , 출력함수 , 삭제함수 , 수정함수 ]
# 등록함수 : 1.입력받기 => 2.객체만들기 => 3.파일처리 [ 4.예외처리 : 오류발생시 다시 입력받기 ]
def set_contact( ) : # 2. 등록 함수
    try :
        name = input(" Name : ")
        phone_number = input(" phone_number : ")
        e_mail = input(" e_mail : ")
        address = input(" address : ")
        # 입력받은 4개의 변수를 Contact 클래스의 객체로 선언
        contact = Contact( name , phone_number , e_mail , address)
        # 파일 처리
        file = open("Contactlist.txt" , "a") # a: 이어쓰기
        file.write( contact.name+","+contact.phone_number+","+contact.e_mail+","+contact.address+"\n")
        file.close()
    except Exception :
        print("[[ 실패 ]] : 주소록 등록 실패 [ 관리자에게 문의 ]")

# 출력함수 : 1.파일읽기 => 2.객체 => 3.리스트담기 => 4.리스트출력
def get_contact( ) :
    try:
        file = open( "Contactlist.txt" , "r" )
        c = file.read() # 파일 내용 읽어오기
        cc = c.split("\n") # 회원별 분리
        for i in cc :
            if not i : break # 만약에 회원이 없으면
            ccc = i.split(",") # 각 회원별 변수 분리
            contact=Contact(ccc[0] , ccc[1] , ccc[2] , ccc[3] ) # 각 회원별 객체 만들기
            contactlist.append(contact) # 리스트에 담기
        # 리스트내 객체 정보 호출
        for i in contactlist :
            i.print_info() # 객체 정보 호출
    except Exception :
        print("[[ 실패 ]] : 주소록 출력 실패 [ 관리자에게 문의 ]")
# 삭제함수 : 1.삭제할 연락처를 입력받아 리스트내에서 삭제  => 2.리스트를 파일에 저장
def del_contact( ) :
    try :
        phone_number = input(" delete phone_number : ")
        for i in contactlist : # 리스트내에서 객체 하나씩 호출
            if i.phone_number == phone_number :# 객체내 연락처가 입력받은 연락처가 동일하면
                contactlist.remove(i) # 리스트내에서 삭제
        print("[[ 실패 ]] : 동일한 연락처가 없습니다 ")

        # 파일 쓰기[ 리스트내 모든 객체 ---> 파일 ]
        file = open("Contactlist.txt", "w")
        for j in contactlist:  # 리스트내에서 객체 하나씩 호출
            file.write(j.name + "," + j.phone_number + "," + j.e_mail + "," + j.address + "\n")  # 객체 하나씩 쓰기
        file.close()
    except :
        print("[[ 실패 ]] : 주소록 삭제 실패 [ 관리자에게 문의 ]")

def print_menu( ) :
    print("[[[[ 연락처 관리 프로그램 ]]]]")
    print("1.연락처 등록 ")
    print("2.연락처 출력 ")
    print("3.연락처 삭제 ")
    print("4.연락처 수정 ")
    print("5.프로그램 종료 ")
    menu = int( input("메뉴선택 : ") )
    return menu # 함수 종료되면서 입력받은 값 반환

contactlist = [ ]
# 프로그램 실행
while True :
    try :
        menu = print_menu()
        if menu == 1 :
            set_contact()
        if menu == 2 :
            get_contact()
        if menu == 3 :
            del_contact()
        #if menu == 4 :
        #if menu == 5 :
        if menu < 1 or menu > 5 :
            print("[[경고 알수 없는 번호 입니다]]")
    except Exception as e :
        print("[[경고]] 오류 발생 관리자에게 문의 ")

