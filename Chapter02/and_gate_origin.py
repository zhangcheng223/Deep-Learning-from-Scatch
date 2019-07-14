def AND(x1, x2):
    w1 = 0.5
    w2 = 0.5
    theta = 0.7
    temp = w1*x1+w2*x2

    if temp <= theta:
        return 0
    elif temp > theta:
        return 1

if __name__ == '__main__':
    print(AND(0, 0))  # 输出0
    print(AND(0, 1))  # 输出0
    print(AND(1, 0))  # 输出0
    print(AND(1, 1))  # 输出1
