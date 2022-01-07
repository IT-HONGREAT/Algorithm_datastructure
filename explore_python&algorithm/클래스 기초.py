#클래스 선언 및 활용

class TestClass:

    def __init__(self,what,name):

        self.what = what
        self.name = name
        print("초기화",self.what)

    def user_info_p(self):
        print("name : ",self.name)


test1 = TestClass('test','hong')

test1.user_info_p()
print(id(test1))
print(test1.__dict__)


#self의 이해

class SelfTest:

    def func1():
        print('function1')

    def func2(self):
        print('function2')
        print('self있는함수',id(self))

test2 = SelfTest()

# print(test2.func1())
print(test2.func2())
print(id(test2))

# 객체화 안하고 그냥출력?
print("클래스의 함수를 이제 이해함")
SelfTest.func2(test2)
SelfTest.func1()


#클래스변수와 인스턴스변수

class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Lee')
user3 = WareHouse('Park')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print("클래스변수 stock_num 을 확인해보자",WareHouse.__dict__)


print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

del user1

# print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)