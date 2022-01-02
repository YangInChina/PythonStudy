# 目录？
"""
    DataFrame简介
    DataFrame的创建
    DataFrame基础属性
"""
# DataFrame简介
"""
    Pandas是Python的一个大数据处理模块。Pandas使用一个二维的数据结构
DataFrame来表示表格形式的数据，相比较于NumPy，Pandas可以存储混合的数
据结构，同时使用NaN来表示缺失的数据，而不用像NumPy一样要手工处理缺失
的数据，并且Pandas使用轴标签来表示行和列。
    DataFrame是一个[表格型]的数据结构，由按照一定的顺序排列的多列数据
组成。DataFrame既有行索引也有列索引。
    行索引：index, 0轴, axis=0
    列索引：columns, 1轴, axis=1
    值：values
    DataFrame设计的初衷是将Series的使用场景从一维拓展到多维。DataFrame
将Series按照列合并而成的二维数据结构，每一列单独取出来都是一个Series。
    DataFrame和Series一样，都要用到pandas包，所以：
    import pandas as pd
    from pandas import DataFrame
"""
# DataFrame的创建
"""
    DataFrame([data,index,columns,dtype])
    其中，data要转化为DataFrame的数据；index设置行索引；columns
设置列索引；dtype设置数据类型（使用NumPy数据类型）。

    使用ndarray创建，也可以使用字典创建DataFrame。
    例如：使用ndarray创建DataFrame对象。
        import numpy as np
        from pandas import DataFrame
        
        print(DataFrame(data=np.random.randint(60, 100, size=(2, 3)), index=['期中', '期末'], columns=['张三', '李四', '王五']))
    结果：
            张三  李四  王五
        期中  69  79  81
        期末  72  92  82
        
    使用字典创建（最常用）。
        DataFrame以字典的键作为每一列的名称，以值（一个数组）作为每一列。
        DataFrame会自动加上每一行的索引。
        使用字典创建的DataFrame后，culumns参数（列索引）将不可被使用。
    例子：
        from numpy import *
        from pandas import DataFrame
        
        dic = {'张三': [68, 71], '李四': [94, 61], '王五': [71, 89]}
        df = DataFrame(data=dic, index=['期中', '期末'])
        print(df)
    结果：
            张三  李四  王五
        期中  68  94  71
        期末  71  61  89
    例子：第一个没使用选项，第二个指定行索引和列索引，第三个使用字典创建。
        from numpy import *
        from pandas import DataFrame
        
        a = DataFrame(arange(10).reshape([2, 5]))
        print(a)
        print('#' * 30)
        
        b = DataFrame(arange(10).reshape([2, 5]), index=list('ab'), columns=list('qwxyz'))
        print(b)
        print('#' * 30)
        
        tem_dict = {'name': ['yangwj', 'ywj'], 'age': [28, 29], 'tel': ['10080', '10010']}
        c = DataFrame(tem_dict)
        print(c)
    结果：
           0  1  2  3  4
        0  0  1  2  3  4
        1  5  6  7  8  9
        ##############################
           q  w  x  y  z
        a  0  1  2  3  4
        b  5  6  7  8  9
        ##############################
             name  age    tel
        0  yangwj   28  10080
        1     ywj   29  10010
    
"""
# DataFrame基础属性
"""
    df.shape：返回DataFrame的形状，包括行数、列数
    df.dtypes：返回数据类型
    df.ndim：返回DataFrame的数据维度。
    df.index：返回DataFrame的行索引。
    df.columns：返回列索引。
    df.values：返回对象值，二维ndarray数组。
    例子：
        from numpy import *
        from pandas import DataFrame
        
        a = DataFrame(data=random.randint(10, 100, (3, 4)))
        print(a)
        print("#" * 30)
        print(a.shape)
        print(a.dtypes)
        print(a.ndim)
        print(a.index)
        print(a.columns)
        print(a.values)
    结果：
            0   1   2   3
        0  61  49  89  53
        1  86  99  44  39
        2  92  26  78  58
        ##############################
        (3, 4)
        0    int32
        1    int32
        2    int32
        3    int32
        dtype: object
        2
        RangeIndex(start=0, stop=3, step=1)
        RangeIndex(start=0, stop=4, step=1)
        [[61 49 89 53]
         [86 99 44 39]
         [92 26 78 58]]
    
"""

