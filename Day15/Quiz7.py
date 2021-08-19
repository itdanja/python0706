
#문제6 : 체스[ 나이트가 이동할수 있는 경우의수 ]

def solution( pos ):
    # 나이트가 움직일수 있는 좌표
    dx = [1,1,-1,-1,2,2,-2,-2]
    dy = [2,-2,-2,2,1,-1,-1,1]
    cx = ord(pos[0]) - ord("A")
    cy = ord(pos[1]) - ord("0") - 1
    result = 0
    for i in range(8):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
            result += 1

    return result

pos = "A7" # 나이트의 위치
result = solution( pos )
print( "문제6 결과 : " , result )
