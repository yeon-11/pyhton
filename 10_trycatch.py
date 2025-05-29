x = 1
if not type(x) is int:  # 만약 변수  x에 타입이 숫자가 아니라면
    raise typeError("숫자를 적어야지 문자를 왜 적어")

# 개발자는 개발자가 정하는 조건이 발생할때 사용자 정의 오류를 만듬
try:
    print("펭귄이여 오라 " + "hello peguin world")
except:
    print("당근당근! 오류났음!")
else:
    print("대박! 너 완전 **파이선 개발자 모드**잖아!")

try:
    f = open("demofile.txt")
    try:
        f.write("눝눝")
    except:
        print("글 못쓰세요")
    finally:
        f.close()
except:
    print("오류났대용")

'''
1. try: 코드블럭에 오류가 있없 테스트
2. except: 사용하면 오류 처리
3. else: 오류 없을때 코드 실행
4. finally: 코브블록에 결과와 상관없이 코드 실행 
'''
