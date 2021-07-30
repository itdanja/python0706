# 구성
# 1.게시물 클래스 설계
# 2.게시물 작성시 클래스기반으로 객체 만들기
# 3.객체를 리스트 저장
# 4.프로그램 시작될때 파일 불러오고 프로그램 끝날때 파일 저장하기

from datetime import datetime # 날짜관련 함수 제공

class board :
    #초기값 [ 객체 선언시 객체에 포함되는 변수들 ]
    def __init__(self , num , title , contents , writer , date , count ):
        self.num = num
        self.title = title
        self.contents = contents
        self.writer = writer
        self.date = date
        self.count = count
    def boardview(self):
        print( str(self.num)+"\t\t"+self.title+"\t\t"+self.writer+"\t\t"+str(self.count)+"\t\t"+self.date )

def start() : # 프로그램 시작 함수
    boardlist = [ ]
    # 기존 파일의 게시물 불러오기
    파일2 = open( "boardlist.txt" , "r")

    b = 파일2.read() # 데이터 모두 읽어오기
    bb = b.split("\n") # 게시물간 분해
    for i in bb :
        if not i : break
        # , 기준으로 분해
        bs = i.split(",")    # 문자열.split("기준문자") : 기준문자 기준으로 분해
        # 분해된 변수를 객체에 생성 [ 분해된 변수를 객체로 하나로 합치기 ]
        temp = board( bs[0] , bs[1] , bs[2] , bs[3] , bs[4] , bs[5] )
        # 객체 다시 리스트에 담기
        boardlist.append(temp)

    파일2.close

    while True :
        print( "\n[[[[[ 커뮤니티 ]]]]] ")
        # 모든 게시물 출력
        print("번호\t\t제목\t\t작성자\t\t조회수\t\t작성일")
        for i in boardlist :
            i.boardview()
        ch = int( input("1.글쓰기 2.글보기 3.종료") )
        if ch == 1 :
            print("[[[ 글 쓰기 페이지 ]]]")
            title = input("제목 : ")
            contents = input("내용 : ")
            writer = input("작성자 : ")
            date = str(datetime.today().month) +"-"+str(datetime.today().day)
            num = len(boardlist) # 리스트 길이
            # 객체 생성
            temp = board( num , title , contents , writer , date , 0 )
            # 리스트에 저장
            boardlist.append(temp)
        if ch == 3 :
            # 리스트를 파일에 저장하기
            파일 = open("boardlist.txt" , "w") #파일 쓰기

            for i in boardlist :
                파일.write( str(i.num) +","+i.title+","+i.contents+","+i.writer+","+i.date+","+str(i.count)+"\n")
                # 변수 구분을 위한 변수들 사이에 , 부분                                            # \n 게시물간 구분
            파일.close() # 파일 닫기
            return # 함수 종료 [ 반환이 없는 그냥 종료 ]

start()