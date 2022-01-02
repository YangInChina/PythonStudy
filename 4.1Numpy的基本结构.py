# Numpy简介
"""
    NumPy（Numerical Python）是Python语言的一个扩展程序库，
是Python中的一个矩阵计算包，支持大量的维度数组与矩阵运算，
功能类似于MATLAB的矩阵运算。此外也针对数组运算提供大量的
数学函数库。
    NumPy系统是Python的一种开源的数值计算扩展，是一个用
Python实现的科学计算包。包括如下内容：
    1）一个具有矢量算数运算和复杂广播能力的快速且节省空间
的多维数组，称为ndarray（N-dimensional array object）；
    2）用于对整组数据进行快速运算的标准数学函数，ufunc
（universal function object）；
    3）用于整合C/C++和Fortran代码的工具包；
    实用的线性代数、傅里叶变换和随机生成函数。NumPy和稀疏矩阵
运算包SciPy（Scientific Python）配合使用更加方便。
    Anaconda自带NumPy，不用额外安装。使用NumPy之前利用如下命令
导入这个库：import numpy as np
"""
# NumPy Ndarray对象
"""
    NumPy最重要的一个特点是其N维数组对象darray，它是一系列同
类型数据的集合，以0下标为开始进行集合中元素的索引。
    ndarray对象是用于存放同类型元素的多维数组。
    ndarray中的每个元素在内存中都有相同存储大小的区域。
    ndarray内部由以下内容组成：
        1）一个指向数据（内存或内存映射文件中的一块数据）的指针。
        2）数据类型或dtype，描述在数组中的固定大小值的格子。
        3）一个跨度元组（stride），其中的整数指的是为了前进到当
    前维度的下一个元素需要“跨过”的字节数。
"""
# NumPy的数据类型
"""
    bool、int（一般为32或64）、int8（一个字节）、int16、int32、
int64、uint8（无符号整型，一字节0~（2**8）-1）、uint16、uint32、
float16、float32、float64、complex64（分别用32位浮点表示实部和虚部）、
complex128或complex()
"""
# NumPy数组属性
"""
    NumPy数组的维数称为秩（rank），一维数组的秩为1，二维数组的秩为2，
以此类推。
    在NumPy中，每一个线性的数组称为一个轴（axis），也就是维度（dimensions）。
比如说，二维数组相当于是两个一维数组，其中第一个一维数组中每个元素又是一个一维数组。
所以一维数组就是NumPy中的轴（axis），第一个轴相当于是底层数组，第二个轴是底层数组里
的数组。而轴的数量——秩，就是数组的维数。
    比较重要的ndarray对象属性：
        ndarray.ndim：秩，即轴的数量或维度的数量。
        ndarray.shape：数组的维度，对于矩阵，n行m列
        ndarray.size：数组元素的总个数相当于.shape中的n*m
        ndarray.dtype：ndarray对象的元素类型
        ndarray.itemsize：ndarray对象中每个元素的大小，以字节为单位。
        ndarray.flags：ndarray对象的内存信息。
        ndarray.real：ndarray元素的实部。
        ndarray.imag：ndarray元素的虚部。
        ndarray.data：包含实际数组元素的缓冲区，由于一般通过数组索引获取元素，所以通常不需要使用这个属性。
        
    下来几个属性的使用：
        ndarray.ndim:用于返回数组的维数，等于秩。
    如：下列先建立一个值为0~23的一维数组，输出其维数；然后改变数组形状，再次输出其维数。
        import numpy as np
        
        a = np.arange(24)
        print(a.ndim)
        b = a.reshape(2, 4, 3)  # 分别为三个维度的数量，乘起来和元素个数必须一致。
        print(b.ndim)
    结果：
    1
    3
        
        ndarray.shape:表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即ndim。比如，一个二维数组，其维度表示“行”和“列”数。
    如：下列构建一个两行三列的数组，输出其形状，即数组的行数和列数。
        from numpy import *
        
        a = array([[1, 2, 3], [4, 5, 6]])
        print(a.shape)
    结果：
    (2, 3)
    shape也可用于调整数组的大小。
    例如：构建一个两行三列的数组，使用shape修改并输出调整后的数组。
        from numpy import *
        
        a = array([[1, 2, 3], [4, 5, 6]])
        print(a)
        print("a的形状为：", end='')
        print(a.shape)
        print('将其修改后的形状为：')
        a.shape = (3, 2)
        print(a)
    结果：
        [[1 2 3]
         [4 5 6]]
        a的形状为：(2, 3)
        将其修改后的形状为：
        [[1 2]
         [3 4]
         [5 6]]
    当然还有reshape（）
    如：
        from numpy import *
        
        a = array([[1, 2, 3], [4, 5, 6]])
        b = a.reshape(3, 2)
        print(b)
    结果：
        [[1 2]
         [3 4]
         [5 6]]
    .itemsize：以字节的形式返回数组中每一个元素的大小。
    例如：下列输出了数据类型为int8和float64的元素所占的字节数。
        from numpy import *
        
        # 数组的dtype为int8
        x = array([1, 2, 3, 4, 5], dtype=int8)
        print(x.itemsize)
        
        # 数组的dtype现在为float464
        y = array([1, 2, 3, 4, 5], dtype=float64)
        print(y.itemsize)
    结果：
        1
        8
"""
# NumPy创建数组
"""
    利用array()函数创建：
    格式：
        numpy.array(object, dtype = None, copy = True,order = None, subok = False, ndmin = 0)
        object:数组或嵌套的数列
        dtype：数组元素的数据类型，可选
        copy：对象是否需要复制，可选
        order：创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
        subok：默认返回一个与基类类型一致的数组。
        ndmin：指定生成数组的最小维度。
    如：创建一维数组并输出。
        from numpy import *
        
        a = array([1, 2, 3])
        print(a)
    结果：
        [1 2 3]
    例如：创建两行两列并输出。
        from numpy import *
        
        a = array([[1, 2], [3, 4]])
        print(a)
    结果：
        [[1 2]
         [3 4]]
    例如：创建最小维数为2的数组，其中第一维具有5个元素，并输出。
        from numpy import *
        
        a = array([1, 2, 3, 4, 5], ndmin=2)
        print(a)
        print(a.ndim)
        b = a.reshape(5)  # 将其改为一维
        print(b)
        print(b.ndim)
    结果：
        [[1 2 3 4 5]]
        2
        [1 2 3 4 5]
        1
    例如：创建复数一维数组。
        from numpy import *
        
        a = array([1, 2, 3], dtype=complex)
        print(a)
    结果：
        [1.+0.j 2.+0.j 3.+0.j]
    
    利用arange()函数创建数组：创建数值范围并返回ndarray对象，在给定间隔内返回均匀间隔的值。
    格式：np.arrange(start,stop,step,dtype)
    例如：创建一维数组。
        from numpy import *
        
        x = arange(5)
        print(x)
    结果：
        [0 1 2 3 4]
    例如：创建一维数组，类型为float。
        from numpy import *
        
        x = arange(5, dtype=float)
        print(x)
        print(x.dtype)
    结果：
        [0. 1. 2. 3. 4.]
        float64
    例如：创建一维数组，步长为2。
        from numpy import *
        
        x = arange(10, 20, 2)
        print(x)
    结果：
        [10 12 14 16 18]
    利用linspace()函数创建数组：数组由等差数列构成。
    格式：np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    start
    stop
    num：要生成的等步长的样本数量，默认为50
    endpoint：该值为True时，数列包含stop值，反之不包含，默认是True。
    retstep：如果为True时，生成的数组中会显示间距，反之不显示。
    dtype
    例子：生成1到10的具有10个等差元素的一维数组。
        from numpy import *
        
        x = linspace(1, 10, 10)  # 最后一个为生成的元素个数，每个元素是等差的。
        print(x)
    结果：
        [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
    例子：全为1。
        from numpy import *
        
        x = linspace(1, 1, 10)
        print(x)
    结果：
        [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    例子：endpoint为false和True，其效果相当于false->[a,b);true->[a,b]
        from numpy import *
        
        x = linspace(10, 20, 5, endpoint=False)
        print(x)
    结果：
        [10. 12. 14. 16. 18.]
    例子：将retstep设为True。
        from numpy import *
        
        a = linspace(1, 10, 10, retstep=True)
        print(a)
    结果：
        (array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.]), 1.0)
    利用zeros()函数创建数组：创建指定大小的数组，元素以0来填充。
    格式：np.zeros(shape, dtype=float, order='C')
    例子：分别创建元素全为0的float、int的两个一维和一个两行两列的二维。
        from numpy import *
        
        x = zeros(5)
        print(x)
        y = zeros((5,), dtype=int)
        print(y)
        z = zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
        print(z)
    结果：
        [0. 0. 0. 0. 0.]
        [0 0 0 0 0]
        [[(0, 0) (0, 0)]
         [(0, 0) (0, 0)]]
    利用ones()函数创建数组：创建指定大小，1填充。
    格式：np.ones(shape,dtype=None,order='C')
    例如：
        from numpy import *
        
        a = ones(5)
        print(a)
        b = ones((5,), dtype=int)
        print(b)
        c = ones((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
        print(c)
    结果：
        [1. 1. 1. 1. 1.]
        [1 1 1 1 1]
        [[(1, 1) (1, 1)]
         [(1, 1) (1, 1)]]
    利用eye()函数创建对角矩阵。
    格式：np.eye(N, M=None, k=0, dtype=<type 'float'>)
    N:输出方阵（行数=列数）的规模，即行数或劣势。
    k:默认对角线为“1”，其余全为“0”，k为负整数则在左下方第k条对角线全为“1”，其余为“0”。
    例子：N=5。
        from numpy import *
        arr = eye(5)
        print(arr)
    结果：
        [[1. 0. 0. 0. 0.]
         [0. 1. 0. 0. 0.]
         [0. 0. 1. 0. 0.]
         [0. 0. 0. 1. 0.]
         [0. 0. 0. 0. 1.]]
"""

