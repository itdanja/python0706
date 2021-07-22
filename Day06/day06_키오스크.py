

# 변수 : 데이터 저장하는 메모리의 공간 1개
# 리스트 : 데이터 저장하는 여러개의 메모리 공간
    # 인덱스 : 리스트내 요소들이 저장된 순서 번호 [ 0번시작~~ ]

stock = [ 10 , 10 , 10 ] # 1.콜라재고 .2.사이다재고 3.환타재고

while True : # 무한루프( 프로그램 전체 )
    print("[[[ 키오스크 ]]]")
    # 고객이 결제후 장바구니는 초기화
    cart = [0, 0, 0]  # 메뉴 선택할때마다 추가 // 고객마다 초기화
    while True : # 무한루프(고객마다) [ 종료조건 : 결제[4] 했을때 종료
        print("[[[ 메뉴 ]]]")
        print("1.콜라(300원) 2.사이다(400원) 3.환타(500원) 4.결제")
        ch = int(input("메뉴 선택 : "))
        if ch == 1 :
            # 1. 재고가 없을경우 2.장바구니가 재고보다 더 클경우 판매불가
            if stock[0] <= 0 or cart[0] >= stock[0] :
                print("[[ 콜라 재고 준비중]] 선택 불가 ")
            else :
                print("[[콜라을 담았습니다]]")
                cart[0] += 1 # 대입연산자  # cart[0] = cart[0] + 1
        elif ch == 2 :
            if stock[1] <= 0 or cart[1] >= stock[1]:
                print("[[ 사이다 재고 준비중]] 선택 불가 ")
            else:
                print("[[사이다을 담았습니다]]")
                cart[1] += 1  # 대입연산자  # cart[0] = cart[0] + 1
        elif ch == 3 :
            if stock[2] <= 0 or cart[2] >= stock[2]:
                print("[[ 환타 재고 준비중]] 선택 불가 ")
            else:
                print("[[콜라을 담았습니다]]")
                cart[2] += 1  # 대입연산자  # cart[0] = cart[0] + 1
        elif ch == 4 :
            print("[[장바구니 현황 ]]")
            if( cart[0] == 0 and cart[1]==0 and cart[2] == 0 ) :
                print("[[ 추가하신 제품이 없습니다 ]] ")
            else :
                print("제품명 수량 금액")
                if (cart[0] != 0): print("콜라", cart[0], cart[0] * 300)
                if (cart[1] != 0): print("사이다", cart[1], cart[1] * 400)
                if (cart[2] != 0): print("환타", cart[2], cart[2] * 500)
                # 결제 여부 물어보고 결제 했을경우 금액받고 재고 차감
                totalpay = (cart[0] * 300)+(cart[1] * 400)+(cart[2] * 500)
                print("총 결제액 : " , totalpay )
                ch2 = int(input("결제 하시겠습니까? [예]:1  [아니요]:0 "))
                if( ch2 == 1 ):
                    print("[[결제화면]]")
                    pay=int( input("금액을 넣어주세요 : ") )
                    if pay < totalpay :
                        print("[[알림]] 금액이 부족합니다 [결제취소] 장바구니 초기화 됩니다 ")
                        break
                    else :
                        print("[[결제완료]] 주문번호 확인 바랍니다]]")
                        # 결제 성공시 => 재고 차감
                        stock[0] -= cart[0]
                        stock[1] -= cart[1]
                        stock[2] -= cart[2]
                        print("[[잔돈 반환 ]] : " , pay - totalpay )
                        print("[[감사합니다]]")
                        break
                else :
                    print("[[결제취소]] : 장바구니 초기화 됩니다 ")
                    break  # 가장 가까운 반목문 탈출
        else:
            print("[[경고]] 알수없는 번호 입니다")