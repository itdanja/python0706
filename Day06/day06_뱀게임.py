# 파이게임 사용해서 뱀게임

# 1. 게임설정  # pygame 설치 : pygame빨간줄 클릭 => 빨간색 느낌표 => install
import sys

import pygame   #파이게임 관련된 라이브러리 가져오기
from pygame.locals import QUIT , Rect , KEYDOWN , K_UP , K_LEFT , K_RIGHT , K_DOWN
                     # 종료 , 그리기   키보드 누름 , 윗방향키 , 아래방향키 , 오른쪽키 , 왼쪽키
import random # 랜덤 파일 가져오기 => 랜덤 함수 사용하기 위해서

pygame.init() # 파이게임 초기화
화면 = pygame.display.set_mode( (600,600) ) # 화면크기 구성
# 초당 프레임수[ FPS ] => 게임속도
초당프레임 = pygame.time.Clock() #

# 2. 리스트 구성
음식 = [ ]
뱀 = [ ]
# 좌표   튜플 = ( )
( W , H ) = (20,20)

# 3. 함수 : 코드를 미리 작성해서 묶음처리[재활용] ( 1.음식생성 2. 음식이동  3.뱀/음식 그리기 )
def 음식생성() :
    while True :
        위치 = ( random.randint( 0 , W-1)  , random.randint(0 , H-1 ) ) # 난수 생성
                # 가로축 0~19 난수                   # 세로축 0~19 난수
        if 위치 in 음식 or 위치 in 뱀 :   # if 변수 in 리스트 :     리스트내 변수가 포함되어 있으면 true
            continue # 반복문 재시작  [ break : 반복문종료 <-----> continue : 반복문 으로 이동 ]
            # 난수위치에 음식이나 뱀이 존재하면 다시 난수 생성
        음식.append( 위치 ) # 아니면 해당 난수위치를 음식리스트에 추가
        break # 음식 추가후 무한루프 종료

def 음식이동( 위치 ) :    #함수( 인수 )       *인수 : 함수로 들어오는 코드[값]
    i = 음식.index(위치)    # 해당위치의 음식을 찾아서
    del 음식[i]   # 해당 음식 삭제
    음식생성() # 음식생성 함수 호출

def 그리기(  ) :
    화면.fill( (255,255,0) )      # 칼라 ( RGB 주소 ) = 255,255,0 => 노랑
    # 음식 그리기
    for food in 음식 :
        # 리스트내 모든 요소를 하나씩 food 변수에 대입
        pygame.draw.ellipse( 화면 , (0,255,0) , Rect(food[0]*30 , food[1]*30 , 30 , 30 ) )
        # ellipse:타원그리기( 화면이름 , 칼라색상 , 그리기위치( x축 , y축 , 가로길이 , 세로길이 )
    # 뱀 그리기
    for body in 뱀 :
        pygame.draw.rect( 화면 , (0,255,255) , Rect( body[0]*30 , body[1]*30 , 30 , 30 ) )
                # rect : 사각형그리기
    # 해당 메시지 그리기
    # if 메시지 != None :   # 메시지가 존재하면
    #     화면.blit( 메시지 , (150,300) ) # 해당 위치에 메시지 띄우기
    # 화면 새로고침
    pygame.display.update()

# 게임실행
글꼴 = pygame.font.SysFont( None , 80 ) # 글꼴
키 = K_DOWN  # 현재 눌린 키 변수
게임종료 = False # 게임종료 여부 변수
# 처음시작시 좌표의 가운데 뱀 하나 추가 하고 시작
뱀.append( ( int(W/2) , int(H/2) )  )
# 처음시작시 음식 10개 추가
for i in range(10) :
    음식생성() # 음식생성함수 호출

# 게임반복 무한루프
while True :
    # 동작
    for 동작 in pygame.event.get() : #pygame 이벤트에 포함되어 있으면
        if 동작.type == QUIT :    # 동작이 종료이면
            pygame.quit() # 파이게임 종료
            sys.exit()   # 현재 코드도 종료
        elif 동작.type == KEYDOWN : # 키를 눌렀을때
            키 = 동작.key  # 눌러진 키를 키 변수에 저장

    if not 게임종료 : # 게임종료가 아니면
        if 키 == K_LEFT :
            머리 = ( 뱀[0][0] -1  , 뱀[0][1]  )
        elif 키 == K_RIGHT :
            머리 = ( 뱀[0][0] +1 , 뱀[0][1] )
        elif 키 == K_UP :
            머리 = ( 뱀[0][0]  , 뱀[0][1]-1 )
        elif 키 == K_DOWN :
            머리 = ( 뱀[0][0] , 뱀[0][1]+1 )

        # 게임종료 조건 [ x축 y축 밖으로 나갈때 , 뱀 몸에 닿았을대 ]
        if 머리 in 뱀 or 머리[0] < 0 or 머리[0] >= W or 머리[1] < 0 or 머리[1] >= H :
            # 메시지 = 글꼴.render( "game over" , True , (255,255,0) )
            게임종료 = True

        뱀.insert(0 , 머리 ) # 0번째 인덱스에 머리위치 추가 [ 첫번째위치 ]
        if 머리 in 음식 : # 머리가 음식에 닿았을때
            음식이동( 머리 )
        else:
            뱀.pop() # 뒤에서 부터 삭제

    그리기() # 그리기함수 호출 [ 인수에 메시지 전달 ]
    초당프레임.tick(5)

# 점수 기능










































