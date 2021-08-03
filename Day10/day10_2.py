
# 객체지향 pygame 게임
import random

import pygame
from pygame.locals import QUIT , KEYDOWN , K_LEFT , K_RIGHT , K_UP , K_DOWN , Rect

pygame.init() # 파이게임 실행
화면 = pygame.display.set_mode( [600,600] ) # 화면 크기
게임속도 = pygame.time.Clock( ) # 게임속도

# 뱀 클래스 [ 객체지향 ]
class snack :
    # 인스턴스 함수 [ 객체 선언시 초기값 ]
    def __init__(self , pos , point):
        self.bodies = [pos]
        self.point = point
    # 이동 함수
    def move(self , key ): # key : 키보드 입력된
        xpos , ypos = self.bodies[0] # 첫번째 몸 = 머리
        if key == K_LEFT :
            xpos -=1    # x축
        elif key == K_RIGHT :
            xpos +=1
        elif key == K_UP :
            ypos -=1    # y축
        elif key == K_DOWN :
            ypos +=1
        head = ( xpos , ypos )
        # 종료 조건 [ 머리가 몸에 닿거나 화면 가로세로 밖으로 나가면 ]
        is_game_over = head in self.bodies or head[0] < 0 or head[0] >= 가로 or head[1] < 0 or head[1] >= 세로
        # 몸에 머리 추가
        self.bodies.insert( 0 , head )
        # 몸이 음식에 닿았을때
        if head in 음식 :
            i = 음식.index( head ) # 음식 위치와 머리의 위치가 동일하면
            del 음식[i]       # 해당 음식 삭제
            self.point +=1  # 음식 먹은 개수
            음식추가(self) # 삭제후 다른곳에 음식추가
        else :
            self.bodies.pop()
        return is_game_over
    # 뱀 그리기
    def 그리기(self):
        for body in self.bodies :
            pygame.draw.rect( 화면 , (0,0,255) , Rect( body[0]*30 , body[1]*30 , 30 , 30 )  )
음식 = [ ]
( 가로 , 세로 ) = ( 20 , 20 )

#음식추가 함수
def 음식추가( snack ) :
    while True :
        pos = ( random.randint( 0 , 가로-1 ) , random.randint(0 , 세로-1) )
        if pos in 음식 or pos in snack.bodies :
            # 음식이 있는 위치와 뱀의 위치는 제외
            continue # 반복문 다시 실행
        음식.append( pos ) # 아니면 음식 추가
        break # 반복문 탈출
# 그리기 함수
def 그리기( snack , msg , point ) :
    화면.fill( (0,0,0) ) # 화면 배경색

    snack.그리기() # 뱀 그리기
    for food in 음식 :
        pygame.draw.ellipse( 화면 , (0,255,0) , Rect( food[0]*30 , food[1]*30 , 30 , 30 ) )

    if msg != None :  # None : 공백
        화면.blit( msg , (150 , 300 ) )
    if point != None :
        화면.blit( point , (300,300) )

    pygame.display.update( )# 그리기 후에 화면 업데이트

# 설정
key = K_DOWN
msg = None # None 공백 = null
게임종료 = False
snack = snack( (int(가로/2) , int(세로/2) ) , 0 ) # 뱀 생성
myfont = pygame.font.SysFont("malgungothic" , 30) # 폰트
point = None  # None 공백 = null
# 게임설정
for i in range(10) :
    음식추가( snack ) # 음식 10개 생성
# 게임실행
while True :
    for 행동 in pygame.event.get( ) :
        if 행동.type ==QUIT : # 종료 했을때
            pygame.quit()
        elif 행동.type == KEYDOWN : # 키를 눌렀을때
            key = 행동.key # 해당 키를 키에 저장
    if 게임종료 :
        msg = myfont.render(" 게임 종료 [획득 점수 : " + str(snack.point) + "]" , True , (255,255,0) )
        point = myfont.render( str(snack.point) , True , (255,255,0) )
    else :
        게임종료 = snack.move(key) # 게임종료가 아니면 객체 이동

    그리기( snack , msg , point )
    게임속도.tick(5)












