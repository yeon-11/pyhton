class MyNumbers:
    def __iter__(self):
        self.a = 1  # 숫자 1
        return self

    def __next__(self):

        if self.a <= 20:  # if: 반복 중지하고 싶을때 가정법
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration  # 지정이 안되어 있어서


myChild = MyNumbers()
myiter = iter(myChild)

for x in myiter:
    print(x)

'''print(next(myiter))
print(next(myiter))
print(next(myiter))'''

# forEach: 편리한 반복 👉 지정한 만큼 검색
mystr = "banana"
for x in mystr:
    print(x)

mytuple = ("a", "b", "c")

myit = iter(mytuple)  # 개별반복
print(next(myit))
print(next(myit))
print(next(myit))

myStr = "banana"  # 반복 지정된 작업량
myit = iter(myStr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

'''
반복자: 셀수 있는 개수의 값을 담고 있는 객체
◾ 반복 가능한 객체, 모든 값을 탐색
◾ 매서드 __iter__(), __next__()
◾ 리스트, 튜플, 딕셔너리 → 모두 반복 가능
'''
