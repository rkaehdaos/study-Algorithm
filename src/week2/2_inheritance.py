# 상속
# 슈퍼클래스 : 부모
# 서브클래스 : 자식
# 상속의 이유? (기초) : 코드 재사용, 중복 최소화, 가독성, 유지보수

class Car:
    """Parent Class"""

    def __init__(self, type, color):
        self.type = type
        self.color = color

    def show(self):
        return 'Car class "Parent Show Method!"'


class BmwCar(Car):
    """sub class 1"""

    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        """부모의 클래스"""
        self.car_name = car_name

    def show_model(self) -> None:
        return 'Your Car name is : %s' % self.car_name


class BenzCar(Car):
    """sub class 2"""

    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        """부모의 클래스"""
        self.car_name = car_name

    def show_model(self) -> None:
        return 'Your Car name is : %s' % self.car_name

    def show(self):
        super().show() # 부모 메소드 호출
        return 'Car Info: %s, %s, %s ' % (self.car_name, self.type, self.color)


# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')
print(model1.color)  # super
print(model1.type)  # super
print(model1.car_name)  # sub

print(model1.show()) # super
print(model1.show_model())
print(model1.__dict__) ## Super, sub 전부 확인 가능

# overiding
model2 =BenzCar('220d','SUV','black')
print(model2.__dict__)
print(model2.show()) # 부모 클래스 메소드 오버라이드된 자식 메소드

# inherent info
# 모든 클래스는 object를 상속받는다
# mro : 상속정보를 List로 출력
print(BmwCar.mro())
print(BenzCar.mro())
print(Car.mro())


# 다중 상속
class X(): #() 빈 값이면 object와 같은 뜻
    pass
class Y():
    pass
class Z():
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass
class M(B,A,Z):
    pass
print(M.mro())
print(A.mro())

""" 너무 많은 다중 상속은 소스 어렵게 됨"""
