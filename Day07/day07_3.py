
# 도서관리 프로그램 [ 함수 ]
    # 도서 : isbn , 도서명 , 대여여부
# 리스트
booklist = [ ]

#함수
def 도서등록() :
    print(" *** 도서등록 페이지 *** ")
    ISBN = input(" 도서 ISBN : ")
        # 중복체크
    for i in booklist : # for i in 2차원리스트 : 2차원리스트내 하나씩 행[리스트]을 대입
        if ISBN in i : #  if 변수 in 리스트 : 리스트내 변수가 포함되어 있는지
            print( "해당 ISBN은 포함되어 있습니다 [초기메뉴] " )
            return # 함수종료

    도서명 = input(" 도서 명 : ")
    대여여부 = True # 도서등록시 초기값으로 TRUE

    book = [ ISBN , 도서명 , 대여여부 ]
    booklist.append( book )

    print(" [[[ 도서 등록이 되었습니다 ]]] ")

# # 함수
# def 도서대여():

# # 함수
# def 도서반납():


# 함수
def 도서목록():
    print(" *** 도서목록 페이지 ****")
    print("ISBN\t도서명\t대여여부") # 제어문자 \t : tab 들여쓰기
    for i in booklist :
        print(i[0],"\t",i[1] ,"\t", i[2] )

    index =  input( "도서명 검색 : ")
    for i in booklist:
        if index in i :
            print(" 검색결과 : ", index )
            ch = int( input(" 1.대여 2.반납 3. 뒤로가기 "))
            # if ch == 1 :
            #     #도서대여() # 도서대여여부 가 true 인 경우에만 대여
            # if ch == 2 :
            #     도서반납() # 도서대여여부가 false 인 경우에만 반납
            if ch == 3 :
                return


#코드 실행
while True : # 무한루프 [ 종료조건 : 없음 ]
    print("1.도서등록[관리자]")
    print("2.도서목록[검색/대여/반납]")
    ch = int (input("메뉴 선택 : "))
    if ch == 1 :
        도서등록()
    if ch == 2 :
        도서목록()


