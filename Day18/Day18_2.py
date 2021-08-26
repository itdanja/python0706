
# 그래프 : 여러 노드가 서로 연결된 자료구조
    # 1. 지도 , 노선도 , 회로도 등등

# 파이썬으로 그래프 구현 예

class Graph() :
    def __init__(self , size):
        self.SIZE = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size) ]

G1 ,G3 = None , None
G1 = Graph(4) # 사이즈가 4인 그래프 생성
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print(" G1 무방향[노드 연결선(출발점x,도착점x) 그래프 ")
for row in range(4) :  # 행 4번 반복
    for col in range(4) :  # 열 4 번 반복
        print( G1.graph[row][col] , end=" ")
    print()

print(" G3 방향 그래프[ 노드 연결선(출발점o,도착점o) ")
G3 = Graph(4)
G3.graph[0][1] = 1; G3.graph[0][2] = 1
G3.graph[3][0] = 1; G3.graph[3][2] = 1

for row in range(4) :
    for col in range(4) :
        print( G3.graph[row][col] , end=" ")
    print()









