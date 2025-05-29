import json

# API: 데이터 요소
some = '{"name":"지연", "age":30, "city":"의정부"}'  # some: son데이터

parseStr = json.loads(some)

print(parseStr["age"])

x = {"name": "John", "age": 30, "city": "New York"}  # 파이선을 json으로 보내야 할때
y = json.dumps(x)  # 파이선 사전을 json으로 변환
print(y)

'''
json(Java Script Object Notation)
◾ 가벼운 데이터 교환 형식
◾ 언어 독립적, 설명 이해 쉬움
◾ 데이터 읽고 생성하는 코드 사용 가능
    java, php, react, vue 등 사용
◾ python은 import 사용
'''
