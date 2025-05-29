i = 0  # 1부터 시작
while i <= 6:  # i가 6보다 작을때 까지 i는 증가
    print(i)
    i += 1  # 지정된 범위까지 1씩 증가

q = 0
while q < 7:
    print(q)
    if (q == 3):  # 3과 같다면 루프중지
        break  # break : 조건이 참이여도 루프 중지
    q += 1

print("=====================================")
w = 0
while w < 5:
    w += 1
    if w == 2:
        continue  # continu: 지정한 엘리먼트를 건너뛰고 다음 엘리먼트로 넘어감
    print(w)

i = 3
while i < 7:
    print(i)
    i += 1
else:  # else: 조건이 더이상 참이 아닐때 한번 더 실행
    print("seven")

'''
파이선루프 (javascript, react,vue, java)
두개의 기본 루프명령
 ◾ for 루프
 ◾ while 루프
루프를 실행하면 조건이 참이면 명령문 수행
'''
