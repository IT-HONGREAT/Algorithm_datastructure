#상속과 다중상속

# 부모 클래스 => 슈퍼클래스
# 자식 클래스 => 서브클래스

class Car:
    """parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!'

class HCar(Car):
    """sub class"""

    def __init__(self,car_name,tp,color):
        super().__init__(tp,color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name:{}".format(self.car_name)

    def show(self):
        print("sub의 call : ",super().show())
        return 'Car Info : {},{},{}'.format(self.car_name,self.type,self.color)

# 일반 사용

model1 = HCar('hongcar', 'suv', 'blue')

print(model1.color) #부모에서 가져옴
print(model1.type)
print(model1.car_name)
print(model1.show())
print(model1.show_model())
print(model1.__dict__)

#메소드 오버라이딩
model2 = HCar('test1car', 'sports', 'yellow')

print(model2.__dict__)
print(model2.show())

#Parent method Call

model3 = HCar('test2car', 'highclass', 'black')
print(model3.show())

#Inheritance Info
print(HCar.mro())
print(Car.mro())

class X(object):
    pass

class Y(object):
    pass

class Z(object):
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

class M(B,A,Z):
    pass

print(M.mro())
print(A.mro())




class Foo:
    def __init__(self, name ):
        self.name = name

    def speak(self):
        print('I am  ',self.name)

class Bar(Foo):
    def __init__(self,name):
        super().__init__(name)

    def speak(self):
        print('You are',self.name)

b = Bar('Hong')
h = Foo('Hong??')
b.speak()
h.speak()


class Test:
    def __init__(self):
        pass

    def fu(self):
        return "B"

print(Test().fu)


