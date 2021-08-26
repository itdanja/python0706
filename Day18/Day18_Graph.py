
# 자전거 도로 건설을 위한 최소 비용

#그래프 클래스
class Graph() :
    def __init__(self , size):
        self.SIZE = size
        self.graph = [[ 0 for _ in range(size)] for _ in range(size) ]

# 전역변수
nameAry = ["춘천" , "서울" , "속초" , "대전" , "광주" , "부산" ]
춘천 = 0 ; 서울 = 1 ; 속초 = 2 ; 대전 = 3 ; 광주 = 4 ; 부산 = 5

