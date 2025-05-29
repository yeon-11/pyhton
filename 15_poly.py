class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive !!!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):  # 프린트 하는 기능
        print("Sail !")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


myCar = Car("Ford", "Mustang")  # 클래스에 생성자를 기반으로 객체생성
# 클래스는 객체를 만들기위한 금형이다
myBoat = Boat("Ibiza", "Touring 20")
Air = Plane("Boeing", "747")

for x in (myCar, myBoat, Air):
    x.move()

'''
oop → dry
Polymorphism: 다형성 (여러형태)
여러객체나 클래스에서 실행될수 있는 동일한 이름의 메서드, 함수, 연산자
'''
