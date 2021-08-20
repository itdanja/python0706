


#파이썬문제2_문제1 : 인터페이스 이용한 클래스
    # 인터페이스 : 동일한 목적하의 동일한 기능 수행하는 목적
    # 파이썬 자체적으로는 인터페이스 X
    # 추상메소드[함수] : 함수의 이름 정의하고 실제 실행코드 정의X

# metaclass=ABCMeta : 추상클래스이름[ 파이썬 인터페이스X ]
    # 추상클래스 선언
    # class 추상클래스명(metaclass=ABCMeta ) :
       # @abstractmethod
       # def 메소드명( self , 인수 , 인수2 ) :
       #    pass

from abc import * # 추상클래스 선언시

class Book(metaclass=ABCMeta ) :
    @abstractmethod # 추상메소드[추상함수] : 이름만정의하고 실행코드정의X => 다른 클래스에서 정의
    def get_rental_price(self , day):
        pass

# class 클래스명( 추상클래스 ) :
class ComicBook( Book ) :
    def get_rental_price(self , day):
        cost = 500 # 기본 요금
        day -= 2 # 첫 2일간 추가요금 x
        if day > 0 : # 추가요금 발생
            cost += day*200
        return cost

class Novel( Book ) :
    def get_rental_price(self , day):
        cost = 1000 # 기본요금
        day -= 3 # 첫 3일간 추가요금 x
        if day > 0 :
            cost += day * 300
        return cost

def solution( book_types , day ) :
    books = [ ]
    for type in book_types :
        if type =="comic" :     # 해당 책이 코믹이면
            books.append( ComicBook() ) # 코믹객체 생성해서 리스트 저장
        elif type == "novel" :  # 해당 책이 소설이면
            books.append( Novel() ) # 소설객체 생성해서 리스트 저장
    total_price = 0 # 총 가격 변수
    for book in books :
        total_price += book.get_rental_price(day)
                        # 해당 객체의 대여메소드( 대여기간 )
    return total_price


book_types = [ "comic" , "comic" , "novel" ]
day = 4
result = solution( book_types , day )
print( "문제1 결과 : " , result   )
















