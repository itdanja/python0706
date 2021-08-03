# 문제
# 배달음식 전문점 운영
    # 1. 피자가게 클래스 설계도
        #  1. 피자종류 : 1.치즈피자[11000] 2. 포테이토피자[15000] 3.쉬림프피자[14000]
        #  2. 주문 리스트

    # 조건 : 피자가게 3개 만들기
        # 가게 선택해서 피자를 주문하기
class Pizza :
    def __int__(self , name , price ):
        self.name = name
        self.price = price

class PizzaStore :
    def __int__(self):
        self.menu_list = [ ] # 메뉴 리스트
        self.menu_list.append( Pizza("치즈피자" , 11000)  ) # 피자 객체  추가
        self.menu_list.append( Pizza("포테이토피자", 15000) )
        self.menu_list.append( Pizza("쉬림프피자", 14000) )
        self.order_list = [ ] # 주문 리스트

    # 주문 리스트 넣는 함수
    def set_order_list(self , order ):
        self.order_list.append( order )
    # 주문 현황
    def get_order_list(self):
        for i in self.order_list :
            print( i.name )

신촌지점 = PizzaStore()
홍대지점 = PizzaStore()
강남지점 = PizzaStore()

지점목록 = [ 신촌지점 , 홍대지점 , 강남지점 ]

while True :
    print("------- 피자 주문 --------")
    ch =  int( input("1.신촌 2.홍대 3.강남") )
    ch2 = int( input("1.치즈피자 2.포테이토피자 3.쉬림프피자 ") )
    if ch2 == 1: 지점목록[ ch - 1].set_order_list( 지점목록[ch-1].menu_list[0]  )
    if ch2 == 2: 지점목록[ ch - 1].set_order_list( 지점목록[ch-1].menu_list[1] )
    if ch2 == 3: 지점목록[ ch - 1].set_order_list(  지점목록[ch-1].menu_list[2] )

    print(" ------- 피자 주문 현황 --------- ")
    print( 지점목록[0] )
    print( 지점목록[1] )
    print( 지점목록[2] )


