
#파이썬문제_3  문제10
    # 상속 : 해당 클래스로부터 변수,메소드 물려받기
        # 상속받으면 좋은점 ! : 부모클래스의 변수,메소드 사용가능
            # super() : 부모 클래스내 변수,메소드 호출
    # 사용 방법
    # class 슈퍼클래스명() :          # 일반적인 클래스 선언
    # class 서브클래스명(슈퍼클래스명): # 슈퍼클래스로부터 상속받은 서브클래스 선언

        # 서브클래스에서 슈퍼클래스내 변수,메소드 사용 가능

#* Customer : 고객을 나타내는 클래스입니다.
class Customer :
    def __init__(self , id , time , num_of_people):
        self.id = id  #  * id : 고객 식별 번호를 나타냅니다.
        self.time = time #   * time : 고객이 신청한 예약 시간을 나타냅니다.
        self.num_of_people = num_of_people  # * num_of_people : 예약 인원 수를 나타냅니다.

# *  Shop : 가게를 나타내는 클래스입니다.
class Shop :
      def __init__(self):
          self.reserve_list = [ ] #  * reserve_list : 가게에 예약한 고객 리스트입니다.

      def reserve(self , customer ) :  #  * reserve : 고객을 매개변수로 받아
          self.reserve_list.append( customer ) # 예약 고객 리스트에 추가 후
          return True #  true를 return합니다

# * HairShop : 미용실을 나타내는 클래스이며,
class HairShop(Shop) : #  Shop을 상속합니다.
    def __init__(self):
        super().__init__()  # 별도에 리스트를 생성할 필요없다
        # 부모클래스내 리스트를 호출해서 사용

    def reserve(self , customer ):  # 부모님내 메소드를 재정의[ 동일한 메소드명을 새로운 실행코드 변경 ]
        if customer.num_of_people != 1 : # 만약에 예약인원수가 1명이 아니면
            return  False # 거짓 리턴
        for i in self.reserve_list :
            if i.time == customer.time :    # 리스트내 예약된 시간이 있으면
                return  False # 거짓 리턴
        self.reserve_list.append( customer ) # 예약리스트에 예약 추가
        return True

#  * Restaurant는 레스토랑을 나타내는 클래스이며,
class Restaurant(Shop) : # Shop을 상속합니다.
    def __init__(self):
        super().__init__()

    def reserve(self , customer ):
        if customer.num_of_people < 2 or customer.num_of_people > 8 : # * 인원수가 2명 이상 8명 이하인 경우에만 예약받습니다.
            return False
        count = 0 # 예약팀 수
        for i in self.reserve_list :
            if i.time == customer.time : # 리스트내 예약된 시간이 현재예약과 동일하면
                count += 1  # 예약자수 1증가
        if count >= 2 : # 예약자수 2 이상이면
            return False
        self.reserve_list.append( customer ) # 예약리스트에 추가
        return True


def solution( customers , shops ) :
    hairshop = HairShop()  # 헤어샵 클래스를 이용한 객체 생성
    restaurant = Restaurant() # 레스토랑 클래스를 이용한 객체 생성
    count = 0 # 예약 받은 횟수

    for customer , shop in zip(customers , shops ) :
                    # 리스트1요소 , 리스트2요소 in  zip(리스트1 , 리스트2 )
        if shop == "hairshop" :
            if hairshop.reserve( Customer( customer[0] , customer[1] , customer[2] ) ) :
                count += 1
            elif shop =="restaurant" :
                if restaurant.reserve( Customer(customer[0] , customer[1] , customer[2] ) ) :
                    count += 1
    return  count #

customers = [[1000, 2, 1], [2000, 2, 4], [1234, 5, 1], [4321, 2, 1], [1111, 3, 10]]
shops = ["hairshop", "restaurant", "hairshop", "hairshop", "restaurant"]
result = solution( customers , shops )
print(" 문제10 결과는 " , result )


















