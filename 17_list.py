thislist = ["사과", "사과", "바나나", "cherry"]
print(thislist)
# javascript에서 사이즈와 length를 쓰면 가지고있는 수를 count
print(len(thislist))
# 모든 데이터에 유형일수 있다
list2 = [1, 5, 7, "banana", True, False]
# 파이선에 관점에서 리스트인 객체 웹디자인 기능사, 정보처리 산업기사,기사
print(type(list2))  # <class 'list'>
# 생성자를 통해서 리스트를 생성할수 있다
made = list(("one", "two", "three"))
print(made)

'''
리스트: 데이터 컬렉션 저장 유형 중 하나
◾ 정렬 가능, 인덱싱 변경 가능, 중복값 허용
◾ 정해진 순서가 있고 그 순서가 변하지 않음
◾ 항목 추가시 오른쪽에 붙음 (데이터 유형을 가진 객체로 정의)

◾ Tuple: 순서o, 변경x, 중복 o
◾ Set: 순서x, 변경x, 중복x
◾ Dictionary: 정렬 변경o, 중복x
'''
