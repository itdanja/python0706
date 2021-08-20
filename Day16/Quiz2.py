
# 파이썬문제 _ 문제1
# 파이썬 인터페이스X => 추상클래스O

# abclass
from abc import *
class DeliveryStore(metaclass= ABCMeta) : # 추상클래스

    @abstractmethod # 추상메소드[ 선언만하고 실행코드X ]
    def set_order_list(self , order_list ):
        pass

    @abstractmethod
    def get_total_price(self):
        pass # 추상메소드에서는 실행코드 정의 안함 [ 연결된 클래스에서 정의 ]

class Food :
    # 생성메소드
    def __init__(self , name , price ):
        self.name = name
        self.price = price

class PizzaStore(DeliveryStore) :
    # 인스턴스메소드
    def __init__(self):
        menu_names = ["Cheese" , "Potato" , "Shrimp" , "Pineapple" , "Meatball"]
        menu_prices = [ 11100 , 12600 , 13300 , 21000 , 19500 ]
        self.menu_list = [ ]
        for i in range(5 ) :            # 푸드객체(메뉴이름 , 메뉴가격) => 리스트에 저장
            self.menu_list.append( Food(menu_names[i] , menu_prices[i] ) )
        self.order_list = [ ]

    # 추상메소드 정의하기
    def set_order_list(self , order_list ):
        for order in order_list : # 주문들어온 리스트에서 각각 오더리스트에 저장
            self.order_list.append( order )

    # 추상메소드 정의하기
    def get_total_price(self):
        total_price = 0
        for order in self.order_list :  # 주문된 리스트에서
            for menu in self.menu_list :  # 가격들의 메뉴에서
                if order == menu.name  :    # 주문된 제품과 메뉴에서 동일하면
                    total_price += menu.price       # 주문된 제품의 메뉴 가격을 총합계에 더하기
        return  total_price

def solution( order_list ) :
    delivery_store = PizzaStore() # 피자가게 객체 생성

    delivery_store.set_order_list( order_list ) # 피자객체에 주문 넣기
    total_price = delivery_store.get_total_price() # 넣은 주문의 총가격
    return total_price


order_list = ["Cheese", "Pineapple", "Meatball"]
result = solution( order_list)
print( " 문제1 결과 : " , result  )




















