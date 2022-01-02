# NumPy常用函数
"""
    三角函数
    算数运算函数
    复数处理函数
"""
# 三角函数
"""
    其中arr为ndarray对象。
    np.sin(arr)：矩阵arr中的每个元素取正弦，sin(arr).
    np.cos(arr)：矩阵arr中的每个元素取余弦，cos(arr).
    np.tan(arr)：矩阵arr中的每个元素取正切，tan(arr).
    np.arcsin(arr)：矩阵arr中的每个元素取反正弦，arctan(arr).
    np.arccos(arr)：矩阵arr中的每个元素取反余弦，arccos(arr).
    np.arctan(arr)：矩阵arr中的每个元素取反正切，arctan(arr).
    例如：下列创建了具有5个元素的一维数组，计算每个元素的正弦、余弦值及正切值。
        from numpy import *
        
        a = array([0, 30, 45, 60, 90])
        print('不同角度的正弦值')
        print(sin(a * pi / 180))
        print('数组中角度的余弦值')
        print(sin(a * pi / 180))
        print('数组中角度的正切值')
        print(tan(a * pi / 180))
    结果：
        不同角度的正弦值
        [0.         0.5        0.70710678 0.8660254  1.        ]
        数组中角度的余弦值
        [0.         0.5        0.70710678 0.8660254  1.        ]
        数组中角度的正切值
        [0.00000000e+00 5.77350269e-01 1.00000000e+00 1.73205081e+00
         1.63312394e+16]
"""
# 算数运算函数
"""
    加减乘除函数：
    add()
    subtract()
    multiply()
    divide()
    注意：数组必须具有相同的形状。
    例如：下列创建了一个3行3列的二维数组和一个具有3个元素的一维数组，就算两个数组的加、减
    乘、除运算。其中第二个数组自动调整为3行3列的二维数组，其他行的元素与第一行元素相同。
        from numpy import *
        
        a = arange(9, dtype=float_).reshape(3, 3)
        print('第一个数组')
        print(a)
        print('\n')
        print('第二个数组（无需手动调整形状，自动变更为（3, 3））')
        b = array([10, 10, 10])
        print(b)
        print('\n')
        print('两个数组相加')
        print(add(a, b))
        print('\n')
        print('两个数组相减')
        print(subtract(a, b))
        print('\n')
        print('两个数组相乘')
        print(multiply(a, b))
        print('\n')
        print('两个数组相除')
        print(divide(a, b))
    结果：
        第一个数组
        [[0. 1. 2.]
         [3. 4. 5.]
         [6. 7. 8.]]
        
        
        第二个数组（无需手动调整形状，自动变更为（3, 3））
        [10 10 10]
        
        
        两个数组相加
        [[10. 11. 12.]
         [13. 14. 15.]
         [16. 17. 18.]]
        
        
        两个数组相减
        [[-10.  -9.  -8.]
         [ -7.  -6.  -5.]
         [ -4.  -3.  -2.]]
        
        
        两个数组相乘
        [[ 0. 10. 20.]
         [30. 40. 50.]
         [60. 70. 80.]]
        
        
        两个数组相除
        [[0.  0.1 0.2]
         [0.3 0.4 0.5]
         [0.6 0.7 0.8]]
    矩阵的点乘运算函数：
        矩阵的点乘同线代中矩阵乘法的定义，需要满足线代中的条件。对于一维矩阵，计算两者内积。
        矩阵的点乘函数为dot()。
    例如：下列计算两个矩阵的点乘运算。
        from numpy import *
        
        a1 = array([[1, 2, 3], [4, 5, 6]])
        a2 = array([[1, 2], [3, 4], [5, 6]])
        print(a1.shape[1] == a2.shape[0])
        print(a1.dot(a2))
    结果：
        True
        [[22 28]
         [49 64]]
    倒数函数：numpy.reciprocal()函数返回矩阵中每个元素的倒数。
    例如：下列计算矩阵中每个元素的倒数。
        from numpy import *
        
        a = array([0.25, 1.33, 1, 100])
        print('我们的数组为：')
        print(a)
        print('\n')
        print('调用reciprocal')
        print(reciprocal(a))
    结果：
        我们的数组为：
        [  0.25   1.33   1.   100.  ]
        
        
        调用reciprocal
        [4.        0.7518797 1.        0.01     ]
    幂函数：numpy.power()函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。
    例子：下列计算数组中每个元素的平方，及用另一个数组做指数的数组的幂运算。
        from numpy import *
        
        a = array([10, 100, 1000])
        print('我们的数组是')
        print(a)
        print('\n')
        print('调用power()函数')
        print(pow(a, 2))
        print('\n')
        print('第二个数组')
        b = array([1, 2, 3])
        print(b)
        print('\n')
        print('再次调用power()函数')
        print(power(a, b))
    结果：
        我们的数组是
        [  10  100 1000]
        
        
        调用power()函数
        [    100   10000 1000000]
        
        
        第二个数组
        [1 2 3]
        
        
        再次调用power()函数
        [        10      10000 1000000000]
    余数函数：numpy.mod()计算输入数组中相应元素消除后的余数。
    函数numpy.remainder()也产生相同的结果。
    例子：下列计算两个数组相除后的余数。
        from numpy import *
        
        a = array([10, 20, 30])
        b = array([3, 5, 7])
        print('第一个数组')
        print(a)
        print('\n')
        print('第二个数组')
        print(b)
        print('\n')
        print('调用mod()函数')
        print(mod(a, b))
        print('\n')
        print('调用remainder()函数')
        print(remainder(a, b))
        print('\n')
    结果：
        第一个数组
        [10 20 30]
        
        
        第二个数组
        [3 5 7]
        
        
        调用mod()函数
        [1 0 2]
        
        
        调用remainder()函数
        [1 0 2]
    最大值最小值函数：获取整个矩阵、行或者列的最大最小值。
    例子：下列获取二维数组中所有元素的最大值、最小值，以及每一列元素的最大值。
        from numpy import *
        
        array = array([[1, 2, 3], [4, 5, 6]])
        print(array.max())
        print(array.min())
        print(array.max(axis=0))
    结果：
        6
        1
        [4 5 6]
"""
# NumPy统计函数
"""
    利用NumPy库获得矩阵中元素的平均值可以通过函数mean()或
average()，同样的可以获取整个矩阵、行或者列的平均值。average()
可以获得加权平均值。
    例如：下列获取二维数组中所有元素的平均值，以及每一列元素的平均值。
        from numpy import *
        
        array = array([[1, 2, 3], [4, 5, 6]])
        print(array.mean())
        print(average(array))
        print(array.mean(axis=0))
    结果：
        3.5
        3.5
        [2.5 3.5 4.5]
    方差函数：var()，相当于函数mean(abs(x-x.mean())**2)[x减去x的平均值的绝对值的平方的平均值]，其中x为矩阵。
        np.mean():平均值函数；
        abs(x)：绝对值函数；
        mean(x)：平均值函数。
    例如：下列获取二维数组中所有元素的方差，以及每一列元素的方差。
        from numpy import *
        
        a = array([[1, 2, 3], [4, 5, 6]])
        print(a.var())
        print(a.var(axis=0))
    结果：
        2.9166666666666665
        [2.25 2.25 2.25]
    标准差函数：标准差函数std()，与sqrt(mean(abs(x-x.mean())**2))或sqrt(x.var())等价。
    sqrt(x)：算数平方根。
    例如：下例获取二维数组中所有元素的标准差，以及每一列元素的标准差
        from numpy import *
        
        array = array([[1, 2, 3], [4, 5, 6]])
        print('我的数组为：')
        print(array)
        print()
        print('使用array.std()')
        print(array.std())
        print('使用array.std(axix=0),求每一列元素的标准差')
        print(array.std(axis=0))
        print()
        print('使用var()')
        print(sqrt(array.var()))
        print('使用var(axis=0),求每一列元素的标准差。')
        print(sqrt(array.var(axis=0)))
        print()
        print('使用原始公式sqrt(mean(abs(x-x.mean())**2))求')
        print(sqrt(mean(abs(array - array.mean()) ** 2)))
    结果：
        我的数组为：
        [[1 2 3]
         [4 5 6]]
        
        使用array.std()
        1.707825127659933
        使用array.std(axix=0),求每一列元素的标准差
        [1.5 1.5 1.5]
        
        使用var()
        1.707825127659933
        使用var(axis=0),求每一列元素的标准差。
        [1.5 1.5 1.5]
        
        使用原始公式sqrt(mean(abs(x-x.mean())**2))求
        1.7078251276599335
    中位数或中值：按大小排列取中间那个值。numpy.median(x,[axis]),axis可指定轴方向，默认axis=None,对所有数取中值。
    例子：求下列数组的中值：
        from numpy import *
        
        a = array([[1, 2, 3], [4, 5, 6]])
        print('数组为：')
        print(a)
        print()
        
        print('中值为：')
        print(median(a))
        print(median(a, axis=0))
        print(median(a, axis=1))
    结果：
        数组为：
        [[1 2 3]
         [4 5 6]]
        
        中值为：
        3.5
        [2.5 3.5 4.5]
        [2. 5.]
    求和：sun(),可以对行、列或整个矩阵求和。
    例子：二维数组求和。
        from numpy import *
        
        a = array([[1, 2, 3], [4, 5, 6]])
        print(a)
        print(a.sum())
        print(a.sum(0))
        print(a.sum(axis=0))
        print(a.sum(1))
        print(a.sum(axis=1))
        b = a.reshape([1, 2, 3])
        print(b.shape)
        print(b.sum(2))
    结果：
         [[1 2 3]
         [4 5 6]]
        21
        [5 7 9]
        [5 7 9]
        [ 6 15]
        [ 6 15]
        (1, 2, 3)
        [[ 6 15]]
    累计和 或 累加：某位置累计和是指该位置之前（包括该位置）所有元素的和。
    例如[1,2,3,4,5]的累计和为[1,3,6,10,15]。
    函数为：cunsum(),
    例子：还是二维数组：
        from numpy import *
        
        a = array([[1, 2, 3], [4, 5, 6]])
        print(a)
        print(a.shape)
        print()
        print(a.cumsum())
        print()
        print(a.cumsum(0))
        print()
        print(a.cumsum(1))
    结果：
        [[1 2 3]
         [4 5 6]]
        (2, 3)
        
        [ 1  3  6 10 15 21]
        
        [[1 2 3]
         [5 7 9]]
        
        [[ 1  3  6]
         [ 4  9 15]]
    
"""
# NumPy矩阵操作函数
"""
    numpy.reshape函数可以在不改变数据的条件下修改形状。
    格式：numpy.reshape(arr, newshape,order='C')
        order的值='C'--按行读，按行排列；
                  'F'--按列读，按列排列；
                  'A'--原顺序；
                  'K'--元素在内存中出现的顺序
    例子：
        import numpy as np
        
        a = np.array([[1, 2, 3], [4, 5, 6]])
        print('a的形状：', end='')
        print(a.shape)
        print(a)
        print()
        b = a.reshape([3, 2], order='c')
        print('b的形状：', end='')
        print(b.shape)
        print(b)
    结果：
        a的形状：(2, 3)
        [[1 2 3]
         [4 5 6]]
        
        b的形状：(3, 2)
        [[1 2]
         [3 4]
         [5 6]]
    返回指定形状的新数组函数：numpy.resize(arr,shape)
        如果新数组大小大于原始大小，则包含原始数组中的元素的副本。
    其中：arr为要修改大小的数组；shape为返回数组的新形状。
    例如：创建（2,3），修改为（3,2）和（3,3）。
        from numpy import *
        
        a = array([[1, 2, 3], [4, 5, 6]])
        print('第一个数组')
        print(a, end='\n\n\n')
        b = resize(a, (3, 2))
        print('第一个数组的形状：')
        print(a.shape)
        print('\n')
        print('第二个数组的形状：')
        print(b.shape)
        print('\n')
        print('修改第二个数组的大小：')
        b = resize(a, (3, 3))
        print(b)
    修改：
        第一个数组
        [[1 2 3]
         [4 5 6]]
        
        
        第一个数组的形状：
        (2, 3)
        
        
        第二个数组的形状：
        (3, 2)
        
        
        修改第二个数组的大小：
        [[1 2 3]
         [4 5 6]
         [1 2 3]]
    矩阵的转置：arr.transpose()和arr.T。
    例子：
        from numpy import *
        
        arr = random.randint(0, 10, (2, 3))
        print(arr)
        print(arr.transpose())
        print(arr.T)
    结果：
        [[9 2 0]
         [3 2 8]]
        [[9 3]
         [2 2]
         [0 8]]
        [[9 3]
         [2 2]
         [0 8]]
    矩阵的逆：
    例子：
        from numpy.linalg import *
        from numpy import *
        
        arr = random.randint(0, 10, (3, 3))
        print(arr)
        print(inv(arr))
        
        arr = eye(3)
        print(arr)
        print(inv(arr))
    结果：
        [[7 8 1]
         [4 7 3]
         [9 0 7]]
        [[ 0.18014706 -0.20588235  0.0625    ]
         [-0.00367647  0.14705882 -0.0625    ]
         [-0.23161765  0.26470588  0.0625    ]]
        [[1. 0. 0.]
         [0. 1. 0.]
         [0. 0. 1.]]
        [[1. 0. 0.]
         [0. 1. 0.]
         [0. 0. 1.]]
    修改元素：
        from numpy import *
        
        arr_i = array([7, 4, 5, 2, 7, 5])
        # 转换数据类型为浮点型。
        arr_f = arr_i.astype(float)
        print(arr_f)
    结果：
        [7. 4. 5. 2. 7. 5.]
    例如：
        from numpy import *
        
        arr = arange(125).reshape([5, 5, 5])
        # 将arr的前三个模块的第三行的第四列元素修改为2333
        arr[0:3, 2, 3] = 2333
        print(arr)
    结果：
        [[[   0    1    2    3    4]
          [   5    6    7    8    9]
          [  10   11   12 2333   14]
          [  15   16   17   18   19]
          [  20   21   22   23   24]]
        
         [[  25   26   27   28   29]
          [  30   31   32   33   34]
          [  35   36   37 2333   39]
          [  40   41   42   43   44]
          [  45   46   47   48   49]]
"""

