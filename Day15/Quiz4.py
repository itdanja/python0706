
#문제9

def func( record ) : # 이기는 경우의수를 찾는 함수
    if record == 0 : # 가위일때
        return 1 # 바위
    elif record == 1 : # 바위일때
        return 2 # 보
    return 0 # 보일때 가위

def solution( recordA , recordB ) :
    result = 0 # A가 계단을 오른 수
    for i in range( len(recordA) ) : # 최대 게임수까지 반복
        if recordA[i] == recordB[i] : # A와 B가 동일한 수를 냈을때
            continue # 반복으로 이동 # 제자리
        elif recordA[i] == func( recordB[i] ) : # 이기는 경우의수
            result += 3 # 3칸 올라가기
        else:   # 졌을때는
            result = max( 0 , result -1 ) # 0보다 더 작은수 제한 # 한칸내려가기
    return result

# 0 : 가위  1:바위  2:보
recordA = [2,0,0,0,0,0,1,1,0,0]
recordB = [0,0,0,0,2,2,0,2,2,2]
result = solution( recordA , recordB )
print(" 문제9의 결과는 " , result )
