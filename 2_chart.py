import matplotlib.pyplot as plt #그래프 그리는 모듈
import numpy as np #숫자에 관련된 파이선라이브러리

y = np.array([35,25,25,15])
#단일 변수에 여러값을 사용할때 쓰는 솔수션은 어레이(배열)이다

plt.pie(y) #y변수로 그림
plt.show()