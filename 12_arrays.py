cars = ["merecedes", "bmw", "ford"]
print(cars)

cars.append("현대")  # append(): 오른쪽에 요소 추가
print(cars)
cars.pop(1)  # 배열 요쇼제거,  pop(), 인덱스번호 사용
print(cars)

# 배열의 요소에 접근하기 인덱스 번호로 참조합니다 0,1,2
x = cars[0]
y = cars[1]
z = cars[2]
print(x, y, z)

q = len(cars)  # len(lengh): 배열의 길이(갯수)
print(q)

'''
배열의 매서드
append(): 새로 추가
clear(): 모든요소 제거
copy(): 복사
count(): 지정된 값 초기화 
extend(): 리스트에 리스트 추가 
index(): 첫번째 인덱스 지정
insert(): 인덱스 지정 삽입 
    cars.insert(3, "sm")
pop(): 지정한 인덱스 요소 제거
remove(): 동일한 값이 여러게 있을때 첫번째 엘리먼트만 제거
reverse(): 순서 반대로
sort(): 글자순대로 정렬 (a~z, ㄱ~ㅎ)
'''

# 가로가 아닌 지정된 범위 만큼 출력
for m in cars:  # forEach: 객체 출력
    print(m)

'''
단일변수에 여러값을 담을때 사용 (js: array)
python에서는 list 사용 (array 사용할시 Numpy 설치)
'''
