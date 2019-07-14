# 导入numpy库
import numpy as np

# 生成NumPy数组
x=np.array([1.0, 2.0, 3.0])
print(x)
type(x)

# Numpy的算术运算
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
x+y
x*y
x/y

# NumPy的N维数组
A = np.array([[1, 2],[3, 4]])
print(A)
print(A.shape)
print(A.dtype)

B = np.array([[3,0],[0,6]])
print(A+B)

# 广播的例子
print(A*10)
C = np.array([10,20])
print(A*C)

#1.5.6 访问元素
X = np.array([[51, 55], [14,19], [0, 4]])
print(X)
print(X[0])         # 第0行
print(X[0][1])      # X(0,1)的元素
for row in X:
    for column in row:
        print(column)

X = X.flatten()       # 将X转化为一维数组
print(X)
print(X[np.array([0,2,4])])
print(X>15)
print(X[X>15])
