#문제2 :
def soultion( shirt_size ) :
    # size_counter = [ 0 , 0 , 0, 0 , 0, 0 ]
    size_counter = [ 0 for _ in range(6) ]
    for shirt in shirt_size :
        # for 변수 in 리스트 : 리스트내 요소를 하나씩 변수에 대입하면서 반복
        if shirt =="XS" : # 만약에 셔츠가 XS
            size_counter[0] += 1 # [0] 인덱스에 +1
        if shirt =="S" :
            size_counter[1] += 1
        if shirt == "M" :
            size_counter[2] += 1
        if shirt == "L" :
            size_counter[3] += 1
        if shirt == "XL":
            size_counter[4] += 1
        if shirt == "XXL":
            size_counter[5] += 1

    return size_counter # 개수를 센 리스트 반환

shirt_size = ["XS" ,"M" , "L" , "L" ,"XL" , "S" , "XXL" ,"M"]

print( " 실행 결과 : " , soultion(shirt_size ) )

#문제3 :
def solution2( number ) :
    count = 0 # 박수 개수

    for i in range( 1 , number+1 ) : # i는 1부터 40까지 1씩증가하면서 반복
        current = i # 현재 수 변수
        while current != 0 : # 현재 수가 0 이면 종료 [ 루프 ]
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9 :
                # 1의 자릿수 3 6 9 찾기
                count += 1
            # 다음의 자릿수 구하기 위해
            current = current // 10     #  // 몫    % 나머지   / 나누기
    return count # 박수 개수 리턴

number = int( input("몇까지 출력할까요? ") )
print("입력하신 수까지의 박수 개수 : " , solution2(number) )

# 문제4 : 리스트 뒤집는 함수
def solution3( arr ) :
    left = 0  # 가장 왼쪽의 인덱스
    right = len(arr)-1  # 가장 오른쪽의 인덱스
    # len( 리스트 ) : 리스트내 요소 전체 수 [ 리스트 길이 ]
    while left < right :
        # 스왑 [ 교환 ]
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        # arr[left] , arr[right] = arr[right] , arr[left]
        # 왼쪽 한칸 이동  / 오른쪽 한칸 이동
        left += 1
        right -= 1
    return arr
arr = [ 1 , 4 , 2 , 3 ]
print(" 리스트 뒤집기 후 : " , solution3(arr) )



