
# 파이썬에서 메일 전송 라이브러리
import smtplib # 메일전송 관련 함수 제공
    # SMTP : Simple Mail Transfer Protocol
    # Protocol : 통신 규약
from email.mime.text import MIMEText # 전자우편 형식 프로토콜

def sendemail( toemail , title , contents ) :
    # 1. 설정
    보내는사람 = "kgs2072@naver.com"   # 실제 본인 메일 주소
    보내는사람비밀번호 = "#"
    smtpname = "smtp.naver.com" # 네이버회사 smtp 서버 주소
    smtpport = 587              # 네이버회사 port 번호     [ 서버로 들어가는 길 번호 = 통신 번호 ]

    # 2. 내용
    msg = MIMEText( contents ) # 메일 내용
    msg["Subject"] = title       # 메일 제목
    msg["From"] = 보내는사람
    msg["To"] = toemail

    # 3 . 전송
    send = smtplib.SMTP( smtpname , smtpport )      # 서버주소 , 포트번호 연결
    send.starttls( ) # TLS 보안 처리
    send.login( 보내는사람 , 보내는사람비밀번호 ) # 보내는사람의 계정 로그인 확인
    send.sendmail( 보내는사람 , toemail , msg.as_string() ) # 문자열로 변환해서 보내기
    send.close()

memberemails = [ "kgs2072@naver.com" , "itdanja@kakao.com" , "kgs2072@naver.com" , "itdanja@kakao.com"    ]

#메일 전송 프로그램
while True :
    print("메일 전송 프로그램 ")
    print(" 1. 메일쓰기 2.회원에게 모두 보내기 3. 종료")
    ch = int(input(" 기능 선택 : "))
    if ch == 1 :
        toemail = input(" 받는사람 메일주소 : ")
        title = input(" 제목 : ")
        contents = input(" 내용 : ")
        sendemail( toemail , title , contents )
        print(toemail, "에게 전송 성공 ")
    if ch == 2 :
        title = input(" 제목 : ")
        contents = input(" 내용 : ")
        for toemail in memberemails :
            sendemail( toemail , title , contents )
            print( toemail ,"에게 전송 성공 ")
    if ch == 3 :
        break
