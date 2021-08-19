
#문제8
def solution( N , votes ) :
    # 후보자의 인원수만큼 리스트 요소 선언
    vote_counter = [ 0 for i in range(N) ]
    # 투표번호에 해당하는 후보리스트에 +1
    for i in votes :
        vote_counter[i-1] += 1
    # 가장 많은 투표 번호를 받은 후보
    maxvote = max( vote_counter ) # 가장 많이 받은 투표수
    result = [ ] # 동점자가 있을경우 리스트
    for idx in range( 0 , N ) :
        if vote_counter[idx] == maxvote :
        # 만일 현재 인덱스가 가장많이 받은 투표수 와 동일하면
            result.append( idx+1 ) # 결과에 추가
    return result

N1 = 5
votes1 =[1,5,4,3,2,5,2,5,5,4]
result = solution( N1 , votes1 )
print( "문제8의 결과1 : " , result )

N2 = 4
votes2 = [1,3,2,3,2]
result = solution( N2 , votes2 )
print( "문제8의 결과1 : " , result )



