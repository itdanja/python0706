# 파이썬문제_4  문제10

#   * Job : 직업을 나타내는 클래스입니다.
class Job :
    def __init__(self): #   직업의 급여를 나타냅니다. 초기 급여는 0입니다.
        self.salary = 0
    def get_salary(self): #  직업의 급여를 return 합니다.
        return self.salary
#   * PartTimeJob : 아르바이트를 나타내는 클래스이며
class PartTimeJob( Job ) : # Job을 상속합니다.
    def __init__(self , work_hour , pay_per_hour ):
        super().__init__() # Job 클래스서 초기 급여 가져오기
        self.work_hour = work_hour
        self.pay_per_hour = pay_per_hour
    # * 아르바이트는 기본적으로 `아르바이트를 한 시간 X 시간 당 급여`를 받으며 40시간 이상 근무시 8시간만큼의 급여를 추가로 받습니다.
    def get_salary(self):
        self.salary = self.work_hour * self.pay_per_hour
        if self.work_hour >= 40 :
            self.salary += (self.pay_per_hour*8 )
        return self.salary
# SalesJob : 판매사원을 나타내는 클래스이며
class SalesJob( Job ) :
    def __init__(self , sales_result , pay_per_sale):
        super().__init__()
        self.sales_result = sales_result
        self.pay_per_sale = pay_per_sale
     # * 판매사원은 기본적으로 `판매실적 * 판매실적 당 급여`를 받으며 판매실적이 10건이 넘으면 급여를 2배로, 20건이 넘으면 급여를 3배로 받습니다.
    def get_salary(self):
        if self.sales_result > 20 :
            self.salary = self.sales_result * self.pay_per_sale * 3
        elif self.sales_result > 10 :
            self.salary = self.sales_result * self.pay_per_sale * 2
        else:
            self.salary = self.sales_result * self.pay_per_sale
        return self.salary

def solution( part_time_jobs , sales_jobs  ) :
    result = 0
    for p in part_time_jobs :
        part_time_jobs = PartTimeJob( p[0] , p[1] )
        result += part_time_jobs.get_salary()
    for s in sales_jobs :
        sales_jobs = SalesJob( s[0] , s[1] )
        result += sales_jobs.get_salary()
    return result

part_time_jobs = [[10, 5000], [43, 6800], [5, 12800]]
sales_jobs =  [[3, 18000], [12, 8500]]
print(" 결과 " , solution( part_time_jobs , sales_jobs ))
