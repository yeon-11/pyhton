# min 평균값
import numpy
import matplotlib.pyplot as plt  # pip install matplotlib
from scipy import stats  # pip install scipy

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
x = numpy.mean(speed)
print(x)
print("===============================================")

# =median(): 중앙값은 모든 값을 정렬한 후 중앙에 있는 값
# 가운데에 숫자가 2개 있을경우 /2를 사용합니다
x = numpy.median(speed)
print(x)
print("===============================================")

# Scipy: 일반적인 값이 mode 가장 많이 나타나는 값 (넘파이 기반으로 하는 과학적 파이선라이브러리)

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
x = stats.mode(speed)
print(x)
print("===============================================")

'''
◾ 표준편차: 값들이 얼마나 펴져있는지 나타내는 숫자
◾ 낮은 표준편차: 대부분의 숫자가 평균값에 가깝다
◾ 표준편차가 높은것: 값이 더 넓은 범위에 펴져있는것
◽ NumPy std(): 메서드를 사용해서 표준편차를 구함
'''
speed = [86, 87, 88, 86, 87, 85, 86]
x = numpy.std(speed)
print(x)
print("===============================================")

'''
Variance: 분산 
◾ 값들이 얼마나 퍼져있는지 나타내는 숫자
◾ 분산의 제곱근을 구하면 표준 편차 나옴
◾ 반대로 표준 편차를 그 자체로 곱하면 분산이 나옴
◾ Numpy에 var() 매서드를 사용하여 분산을 구함
'''
speed = [32, 111, 138, 28, 59, 77, 97]
x = numpy.var(speed)
print(x)

x = numpy.std(speed)
print(x)
print("===============================================")

'''
백분위수
◾ 통계에서 특정비율의 값이 그 값보다 낮은 정도를 나타내는 숫자를 제공하는데 사용 
'''
ages = [49, 55, 44, 23, 27, 24, 29, 23, 27, 24, 29, 30, 23, 27, 24, 29, 22]
x = numpy.percentile(ages, 75)
print(x)
x = numpy.percentile(ages, 50)
print(x)
print("===============================================")

'''
머신러닝 
◾ 컴퓨터가 데이터와 통계를 연구하여 학습하도록 하는것
◾ 머신러닝은 데이터를 분석하고 결과를 예측하는 방법을 배우는 프로그램
◾ 데이터 세트: 컴퓨터의 관점에서 데이터 세트는 데이터 집합
◾ 배열부터 완전한 데이터베이스까지 무엇이든 (평균에 대한 통계 낼 수 있음)
◾ 머신러닝에서는 매우 큰 데이터 세트를 다루는 것이 일반적
◾ 평균 중앙값 모드
'''

# 20250612 데이터 분포 Data Distribution
# 아래 0~5 사이의 난수 250개를 포함하는 배열
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)

plt.hist(x, 5)
plt.show()
print("===============================================")

x = numpy.random.uniform(0.0, 5.0, 100000)
print(x)

plt.hist(x, 100)
plt.show()
print("===============================================")

# 정규 데이터 분포 Normal Data Distribution
# 주어진 값을 중심으로 값이 집중된 배열
# 확률론에서 이러한 종류의 데이터 분포는 정규데이터 분포 또는 가우스데이터 분포
x = numpy.random.normal(5.0, 1.0, 100000)
# 평균값 5.0, 표준편차 1.0 값이 4 ~ 6 사이에 있음. 최고값 5.0

plt.hist(x, 100)
plt.show()
print("===============================================")

# 무작위 데이터분포
# 첫번째 배열: 평균 5, 표준편차 1
x = numpy.random.normal(5.0, 1.0, 1000)
# 두번째 배열: 평균 10, 표준편차 2
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()
print("===============================================")

# 선형 회귀 Linear Regression
'''
선형 회귀 Linear Regression
◾ 관계를 찾을때 회귀라는 용어 사용
◾ 머신러닝과 통계 모델링에서는 이러한 관계를 사용하여 미래 이벤트의 결과를 예측
'''
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

plt.scatter(x, y)
plt.show()
print("===============================================")

# scipy 선형 회귀선을 가져와서 그림
'''
slope: 회귀선 기울기 
intercept: 회귀선이 y축과 만나는 지점
r: 피어슨 상관계수 (두 변수간의 선형 상관 정도 👉 -1 ~ 1)
p: 기울기의 유의확률, 0에 가까울수록 통계적으로 유의 
std_err: 표준오차 (기울기 추정치의 표준오차: 적을수록 신뢰도 높음)
'''
slope, intercept, r, p, std_err = stats.linregress(x, y)
# 주어진 x값에 대해서 선형회귀 직선을 기반으로 y값 예측

def myfunction(x):
    return slope * x + intercept

mymodel = list(map(myfunction, x))

plt.scatter(x, y)  # 점 데이터
plt.plot(x, mymodel)  # 회귀선
plt.show()
print("===============================================")

# 속도 예측
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

speed = myfunc(20)
print(speed)