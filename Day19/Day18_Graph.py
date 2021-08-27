
# 자전거 도로 건설을 위한 최소 비용
#그래프 클래스
class Graph() :
    def __init__(self , size):
        self.SIZE = size
        self.graph = [[ 0 for _ in range(size)] for _ in range(size) ]

# 전역변수
nameAry = ["춘천" , "서울" , "속초" , "대전" , "광주" , "부산" ]
춘천 = 0 ; 서울 = 1 ; 속초 = 2 ; 대전 = 3 ; 광주 = 4 ; 부산 = 5

# 그래프 정점 찍는 함수
def printGraph(g) :
    print("   ", end=" ")
    for v in range( g.SIZE ) :
        print( nameAry[v] , end=" ")
    print( )
    for row in range( g.SIZE ) :
        print( nameAry[row] , end= "   ")
        for col in range( g.SIZE ) :
            print( g.graph[row][col] , end="   ")
        print()
    print()

# 특정 정점이 그래프에 연결되어 있는지 확인하는 함수
def findVertex( g , findVtx ) :
    stack = [ ]
    visitedAry = [ ] # 방문한 정점

    current = 0     # 시작 정점
    stack.append( current )
    visitedAry.append( current )

    while len(stack) !=0 :
        next = None
        for vertex in range(gSize) : # 방문한 적이 없는 정점 찾기
            if g.graph[current][vertex] != 0 :
                if vertex in visitedAry : # 방문한 적이 있는 정점이면 탈락
                    pass
                else:
                    next = vertex       # 방문한 적이 없으면 다음 정점으로 지정
                    break
        if next !=None :
            current = next
            stack.append(current)
            visitedAry.append(current)
        else:
            current = stack.pop()

    if findVtx in visitedAry :
        return True
    else:
        return False

# 메인 코드 부분 #
gSize = 6
G1 = Graph(gSize)
# 임의 거리 비용
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40 ; G1.graph[서울][대전] = 11 ; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40 ; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12 ; G1.graph[대전][광주] = 20 ; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20 ; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

print("## 자전거 도로 건설을 위한 전체 연결도 ##")
printGraph(G1)


