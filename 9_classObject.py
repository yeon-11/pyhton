class MyClass:
    x = 5 #프로퍼티

p1 = MyClass() #객체
#임의에 변수 p1 => 부모인 MyClass를 상속받음
print(p1.x)

#유산을 물려주지 않고 스킬을 물려줌
class Person:
    def __init__(self, name, age): #파이선 함수
        self.name = name
        self.age = age

yeon = Person(name="ji-yeon", age=30) #객체
print("내 이름은 ", yeon.name, "이며 나이는 ", yeon.age, "입니다")


'''
파이선: 객체지향 프로그래밍 언어
속성과 메서드를 갖춘 객체
클래스: 객체 생성자나 객체를 만드는 청사진과 같다
'''