# Pandas and Series
# Pandas 简介
"""
    Python Data Analysis Library（Pandas）是基于NumPy的一种工具，该工具是为
了解决数据分析任务而创建的。Panda是纳入了大量库和一些标准的数据模型，提供了
高效地操作大型数据集所需的工具。
    Pandas提供了大量能快捷地处理数据的函数和方法。它是使Python称为强大而高效
的数据分析环境的重要因素之一。
"""
# Pandas数据结构
"""
    Series：一维数组，与NumPy中的一维array类似。它们与Python基本的数据结构List
也很相近，其区别是：List中的元素可以是不同的数据类型，而Array和Series中则只允许
存储相同的数据类型，这样可以更高效的使用内存，提高运算效率。
    Time-Series：以时间为索引的Series。
    DataFrame：二维的表格型数据结构。很多功能与R中的data.frame类似。可以将DataFrame
理解为Series的容器。
    Panel：三维的数组，可以理解为DataFrame的容器。
"""
# 使用 import pandas as pd导入pandas库。
# Series
"""
    一组带索引的数组。
    创建：Series(data=可迭代的一维数组, [index=所应列表, [dtype=数据类型]])
    Series就是竖起来的List。
    例如：创建一个Series对象。
        from pandas import *
        
        a = Series([1, 4, 'ww', 'tt'])
        print(a)
    结果：
        0     1
        1     4
        2    ww
        3    tt
        dtype: object
    例子：创建5个Series对象，
          分别利用Series函数的无选项、
          index选项指定行索引，
          dtype指定数据类型，
          使用NumPy一维数组，
          以及同时指定行索引和元素值的方法创建。
        from pandas import Series
        from numpy import *
        
        print(Series(range(3)))
        print('#' * 30)
        print(Series(range(3), index=['first', 'second', 'third']))
        print('#' * 30)
        print(Series(range(3), index=['first', 'second', 'third'], dtype=int))
        print('#' * 30)
        print(Series(array(range(3)), index=['first', 'second', 'third'], dtype=int))
        print('#' * 30)
        print(Series({'first': 1, 'second': 2, 'third': 3}))
    结果：
        0    0
        1    1
        2    2
        dtype: int64
        ##############################
        first     0
        second    1
        third     2
        dtype: int64
        ##############################
        first     0
        second    1
        third     2
        dtype: int32
        ##############################
        first     0
        second    1
        third     2
        dtype: int32
        ##############################
        first     1
        second    2
        third     3
        dtype: int64
    Series对象的属性有：
        dtype：返回数据类型。
        index：返回索引（可更改）
        values：返回值
        name返回对象的name（可更改）。
        Series.index.name：返回Series对象的索引的name属性（可更改）。
    例子：输出series对象的dtype、index、value、name以及index.name的属性值。
        from pandas import *
        from numpy import *
        
        series0 = Series(array(range(3)), index=["first", "second", "third"], dtype=int)
        print("原本的series为：")
        print(series0)
        print('#' * 30)
        print("原本的索引：", end='')
        print(series0.index)
        series0.index = ["语文", "数学", "英语"]
        print('数据类型为：', end='')
        print(series0.dtype)
        print('#' * 30)
        print('修改后的索引为：', end='')
        print(series0.index)
        print('#' * 30)
        print('series的值为：', end='')
        print(series0.values)
        series0.name = "Series0"
        series0.index.name = 'idx'
        print('#' * 30)
        print('打印现在的series：')
        print(series0)
    结果：
        原本的series为：
        first     0
        second    1
        third     2
        dtype: int32
        ##############################
        原本的索引：Index(['first', 'second', 'third'], dtype='object')
        数据类型为：int32
        ##############################
        修改后的索引为：Index(['语文', '数学', '英语'], dtype='object')
        ##############################
        series的值为：[0 1 2]
        ##############################
        打印现在的series：
        idx
        语文    0
        数学    1
        英语    2
        Name: Series0, dtype: int32
"""
# Series增、删、改、查
"""
    (1).series查询：
        1.常规查询：一是通过索引查询，一是通过下标序号查询。
            import numpy as np
            from pandas import Series
            
            series0 = Series(np.array(range(3)), index=["first", "second", "third"], dtype=int)
            print(series0[1])
            print("#" * 30)
            print(series0["first"])
        结果：     
            1
            ##############################
            0   
        2.切片查询：格式ser[start:end](闭区间)；ser[num1:num2](前闭后开)
            import numpy as np
            from pandas import Series
            
            series0 = Series(np.array(range(3)), index=["first", "second", "third"], dtype=int)
            print(series0["second":"third"])
            print("#" * 30)
            print(series0[1:2])
        结果：
            second    1
            third     2
            dtype: int32
            ##############################
            second    1
            dtype: int32
        条件查询：
            import numpy as np
            from pandas import Series
            
            series0 = Series(np.array(range(3)), index=["first", "second", "third"], dtype=int)
            print(series0[series0 > 0])  
        结果：
            second    1
            third     2
            dtype: int32
    (2).series增加元素：
        1.直接赋值：Series0['third'] = 5;若存在third，则修改，若不存在，则添加。
        2.append()函数：连接两个series，并返回新的合并后的对象，且不改变原series。
            格式：pandas.Series.append(to_append, ignore_index=False, verify_intergrity=False)
                to_append：目标series。
                ignore_index=False：保留原索引，True为重构、新建索引。
                verify_intergrity：True：检测合并后是否有索引冲突，False则不检测。
            from pandas import Series
            
            s = Series([1, 2, 3, 4])
            s = s.append(Series(5, index=[2]), ignore_index=True)
            print(s)
        结果：
            0    1
            1    2
            2    3
            3    4
            4    5
            dtype: int64
    (3)Series删除元素：
        1.Python的del语句：直接通过索引删除。
            from pandas import Series
            
            s = Series([1, 2, 3, 4])
            print(s)
            print("#" * 30)
            del s[3]
            print(s)
        结果：
            0    1
            1    2
            2    3
            3    4
            dtype: int64
            ##############################
            0    1
            1    2
            2    3
            dtype: int64
        2.Series的pop()函数：弹出某个缩印的值，并将其删除。格式：Series.pop(index)    index只能是一个值，不能是序列。
        3.Series的drop()函数：根据索引批量删除数据。
            from pandas import Series
            
            s = Series([1, 2, 3, 4])
            s1 = s.drop([2, 3])
            print(s)
            print("#" * 30)
            print(s1)
        结果：
            0    1
            1    2
            2    3
            3    4
            dtype: int64
            ##############################
            0    1
            1    2
            dtype: int64
    (4)修改元素：
        1.通过索引（或切片）直接修改：
            from pandas import Series
            
            s = Series([1, 2, 3, 4])
            s[0] = 6
            print(s)
            print("#" * 30)
            s[1:3] = 12
            print(s)
        结果：
            0    6
            1    2
            2    3
            3    4
            dtype: int64
            ##############################
            0     6
            1    12
            2    12
            3     4
            dtype: int64
        2.updata()函数：Pandas.Series.updata(other_s)
"""
import numpy as np
from pandas import Series

s = Series([1, 2, 3, 4])
s[0] = 6
print(s)
print("#" * 30)
s[1:3] = 12
print(s)
# s = s.append(Series(5, index=[2]), ignore_index=True)
# series0 = Series(np.array(range(3)), index=["first", "second", "third"], dtype=int)
