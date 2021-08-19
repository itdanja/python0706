
#문제10
def solution( prices ) :

    p_max = 1000001 # 최대 수익
    p_min = p_max # 최저 수익
    result = -p_max  # 현재 수익
    for i in prices :
        if p_min != p_max : # 최대 수익과 최저 수익이 다르면
            result = max( result , i - p_min )
            #현재수익 =
        p_min = min( p_min , i )

    return result

prices1 = [ 1,2,3 ]
result = solution( prices1 )
print(" 문제 10의 결과 : ", result )

prices2 = [ 3,1 ]
result = solution( prices2 )
print(" 문제 10의 결과 : ", result )