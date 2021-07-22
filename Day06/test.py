import pygame # import 파일 가져오기
from pygame.locals import QUIT , Rect , KEYDOWN , K_UP , K_LEFT , K_RIGHT , K_DOWN
                        # 종료 , 직각 ,  키 눌렀을때 , 위키 , 왼쪽키 , 오른쪽키 , 아래키
import random # 랜덤 파일 가져오기 => 랜덤 함수 사용하기 위해
import sys # 시스템 파일 가져오기

pygame.init() #파이게임 초기값
SURFACE = pygame.display.set_mode( (600,600) ) # 화면구성
FPSCLOCK = pygame.time.Clock() # 시간체크

# 리스트 구성
음식 = []
뱀 = []
(W,H) = (20,20) # 가로 세로 위치

# 함수 만들기
def 음식생성():
    while True:
        위치 = ( random.randint( 0 , W-1) , random.randint(0 , H-1) ) #난수 생성
        if 위치 in 음식 or 위치 in 뱀 : # 난수위치에 기존 리스트가 있으면
            continue # 반복문 재시작  <=> break 반복문종료
        음식.append(위치)
        break
def 음식이동( 위치 ) :
    i = 음식.index(위치) # 리스트.index( 값 ) => 해당값의 인덱스 번호
    del 음식[i]   # 해당 인덱스번호 리스트에서 삭제
    음식생성() # 삭제후 새로운 음식 생성

def 그리기( 메시지 ) :
    SURFACE.fill( (0 , 0 , 0) ) # 화면 색상
    for food in 음식 : # 음식그리기
        pygame.draw.ellipse( SURFACE , (0,255,0) , Rect( food[0]*30 , food[1]*30  , 30 , 30) )
            # ellipse 타원그리기( 화면이름 , 칼라색상 , 그리기위치( x축 , y축 , 가로크기 , 세로크기 )
    for body in 뱀 : # 뱀그리기
        pygame.draw.rect( SURFACE , (0,255,255)  , Rect( body[0]*30 , body[1]*30 , 30 , 30 ) )
            # rect : 사각형그리기
    for index in range(20) : # 선그리기
        pygame.draw.line( SURFACE , (64,64,64) , (index*30,0) , (index*30 , 600 )  ) # x축 그리기
        pygame.draw.line( SURFACE , (64,64,64) , ( 0 , index*30 ) , ( 600 , index*30 )) #y축 그리기
            # line : 선 그리기
    if 메시지 !=None : # 해당 메시지가 존재하면
        SURFACE.blit(메시지, (150,300) ) # 해당 위치에 메시지 띄우기
    pygame.display.update()

# 게임 실행
myfont = pygame.font.SysFont( None , 80)
key = K_DOWN # 아래키
메시지 = None
게임종료 = False # 종료 스위치
뱀.append( ( int(W/2) , int(H/2) ) ) # 첫실행시 가운데에 리스트내 항목 추가
for _ in range(10): # 10번 반복실행
    음식생성()
while True :
    for 동작 in pygame.event.get(): #pygame 이벤트 발생
        if 동작.type == QUIT :    # 종료이면
            pygame.quit()       # 종료하기
            sys.exit()
        elif 동작.type == KEYDOWN :   # 키를 눌렀을때
            key = 동작.key    # 눌러진 키를 key 변수에 저장
    ##################################################
    if not 게임종료 : # 게임종료가 아니면
        if key == K_LEFT :
            머리 = ( 뱀[0][0] -1  , 뱀[0][1] ) #머리부분을 X축[왼쪽]으로 이동
        elif key == K_RIGHT :
            머리 = ( 뱀[0][0] +1 , 뱀[0][1] ) #머리부분을 X축[오른쪽]으로 이동
        elif key == K_UP :
            머리 = ( 뱀[0][0] , 뱀[0][1]-1) # 머리부분을 Y축[위]으로 이동
        elif key == K_DOWN :
            머리 = ( 뱀[0][0] , 뱀[0][1]+1) # 머리부분을 Y축[아래]으로 이동

        if 머리 in 뱀 or 머리[0] < 0  or 머리[0] >= W or 머리[1] < 0 or 머리[1] >=H :
            메시지 = myfont.render( "game over" , True , (255,255,0) )
            게임종료 = True

        뱀.insert( 0 , 머리 )
        if 머리 in 음식 :  # 머리가 음식에 포함 되어 있는경우
            음식이동( 머리 ) # 머리위치에 음식을 삭제후에 다른곳에 음식생성
        else :
            뱀.pop()

    그리기(메시지)
    FPSCLOCK.tick(5)



