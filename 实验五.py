# 定义四乘四数组，输出最大值最小值以及他们的行列标，并且输出转置后的数组
from numpy import *
from pandas import *


class Matrix:
    def __init__(self):
        self.__mtx = DataFrame(random.randint(10, 100, size=(4, 4)))
        self.__Maxcol = 0
        self.__Maxrow = 0
        self.__Mincol = 0
        self.__Minrow = 0

    def getMax(self):
        max1 = self.__mtx[0][0]
        for i in range(0, 4):
            for j in range(0, i):
                if max1 <= self.__mtx[i][j]:
                    max1 = self.__mtx[i][j]
                    self.__Maxrow = i
                    self.__Maxcol = j
        print('最大的值为：', end='')
        print(max1)
        print("行列号为：[", end='')
        print(self.__Maxrow, end='')
        print('][', end='')
        print(self.__Maxcol, end='')
        print(']')

    def getMin(self):
        min1 = self.__mtx[0][0]
        for i in range(4):
            for j in range(i):
                if min1 >= self.__mtx[i][j]:
                    min1 = self.__mtx[i][j]
                    self.__Minrow = i
                    self.__Mincol = j
        print('最小的值为：', end='')
        print(min1)
        print("行列号为：[", end='')
        print(self.__Minrow, end='')
        print('][', end='')
        print(self.__Mincol, end='')
        print(']')

    def Show(self):
        print(self.__mtx)

    def Transpose(self):
        temp = 0
        for i in range(4):
            for j in range(i):
                temp = self.__mtx[i][j]
                self.__mtx[i][j] = self.__mtx[j][i]
                self.__mtx[j][i] = temp


if __name__ == '__main__':
    m = Matrix()
    m.getMax()
    m.getMin()
    m.Show()
    m.Transpose()
    print('转置后：\n' + '#' * 30)
    m.Show()
