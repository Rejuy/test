import time
import cmath
import matplotlib.pyplot as plt
import prettytable as pt
import decimal


plt.switch_backend('agg')


def Fibonacci(nStart, increaseType, nLimit, coefficient, function):
    n = nStart

    table = pt.PrettyTable()
    table.field_names = ["n", "1st", "2nd",
                         "3rd", "4th", "5th", "average"]

    final = []
    xValues = []
    yValues = []

    while n <= nLimit:
        result = []
        result.append(n)
        for count in range(1, 6):
            start = time.perf_counter()
            function(n)
            end = time.perf_counter()
            result.append(round(end - start, 6))
        average = 0
        for count in range(1, 6):
            average += result[count]
        average /= 5
        result.append(round(average, 6))
        xValues.append(n)
        yValues.append(average)
        table.add_row(result)
        if increaseType == "+":
            n += coefficient
        else:
            n *= coefficient

    print(table)
    plt.plot(xValues, yValues, c='green')
    plt.title('Time', fontsize=24)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.xlabel('n', fontsize=14)
    plt.ylabel('time', fontsize=14)
    plt.savefig("./" + function.__name__ + ".png")


def outcome(nStart, increaseType, nLimit, coefficient, function):
    n = nStart
    table = pt.PrettyTable()
    table.field_names = ["n", "F(n)"]
    while n <= nLimit:
        result = [n]
        result.append(function(n))
        table.add_row(result)
        if increaseType == "+":
            n += coefficient
        else:
            n *= coefficient
    print(table)


#===============================================#
# 递归计算方法


def Recurrence(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return Recurrence(i - 1) + Recurrence(i - 2)


#Fibonacci(5, "+", 35, 5, Recurrence)
outcome(5, "+", 35, 5, Recurrence)
#=====================================================#
# 迭代计算方法


def Iteration(n):
    index = 3
    a = 1
    b = 1
    c = 0
    while index <= n:
        a = a + b
        c = b
        b = a - b
        index += 1
    return a


#Fibonacci(10, "*", 1000000, 10, Iteration)
outcome(4, "*", 512, 2, Iteration)
#===========================================#
# 通项公式

omega = 1.618


def General(k):

    if k == 1:
        return round(omega, 3)
    if k % 2 == 1:
        base = round(General((k - 1) / 2), 3)
        return round(base * base * omega, 3)
    base = round(General(k / 2), 3)
    return round(base * base, 3)


#Fibonacci(10, "*", 1000000, 10, General)
outcome(4, "*", 512, 2, General)
#=================================================#
# 矩阵乘法
fundation = [[1, 1], [1, 0]]


def multiply(left, right):
    result = [[0, 0], [0, 0]]
    result[0][0] = left[0][0] * right[0][0] + left[0][1] * right[1][0]
    result[0][1] = left[0][0] * right[0][1] + left[0][1] * right[1][1]
    result[1][0] = left[1][0] * right[0][0] + left[1][1] * right[1][0]
    result[1][1] = left[1][0] * right[0][1] + left[1][1] * right[1][1]
    return result


def matrixFunction(k):
    m = []
    if k == 1:
        return fundation
    if k % 2 == 1:
        m = matrixFunction((k-1)/2)
        return multiply(m, multiply(m, fundation))

    m = matrixFunction(k / 2)
    return multiply(m, m)


def Matrix(k):
    return matrixFunction(k - 1)[0][0]


#Fibonacci(10, "*", 1000000, 10, Matrix)
outcome(4, "*", 512, 2, Matrix)
