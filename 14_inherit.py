class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def talking(self):
        print(self.firstname, self.lastname)


class Child(Person):
    pass


q = Child("jiyeon", "park")
q.talking()


class Pr:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


anyOne = Pr("jiyeon", "park")
anyOne.printname()

'''
Python Inheritance 상속
- 부모클래스: 상속(기본)
- 자식클래스: 부모클래스로 부터 상속받음(파생)
'''
