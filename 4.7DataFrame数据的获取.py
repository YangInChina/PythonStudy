# DataFrame数据的获取
"""
    啊这。。。
"""
# Loc的使用
"""
    使用DataFrame的Loc可以获取指定行标签和列标签所对应的数据
格式如下：DataFrame.Loc[index,column]

    例如：定义一个pandas的DataFrame对象
        import pandas as pd
        
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index=list('abc'))
        print(data)
    结果：        
           A  B  C
        a  1  4  7
        b  2  5  8
        c  3  6  9
    假设在此二维表中，想要得到一个具体的值，行列表为bB，则可：data.loc['b','B']
    当然，也可以为某一区间的值：data.loc[start:end, start:end]
        import pandas as pd
        
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index=list('abc'))
        print(data.loc['b':'c', 'B':'C'])
    结果：
           B  C
        b  5  8
        c  6  9
"""
# iloc的使用
"""
    iloc与loc一样，中括号里面也是先行后列，与loc不同的是，iloc
接受的是一个数字，代表着要选择的数据的位置。
    例如：data.iloc[6]：这表示选择是第六行的，而不是值为6的那一行。
          data.iloc[1:2,1:2]：前开后闭，所以只显示第一行第一列的数据。
          data.iloc[1:2]：column缺省时，默认为1。
          data.iloc[[0,2],[1,2]]：即可自由选取行位置，和列位置对应的数据。
    当然，iloc也可以接受一个boolean的array，相当于按照这个表的真假按照位置的顺序选择值。
    例如：下列为输入行标签为True的a，c行的值，和输出第一行的值。
        from pandas import *
        
        data = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], }, index=['a', 'b', 'c'])
        print(data.iloc[[True, False, True]])
        print('#'*30)
        print(data.iloc[1:2])
    结果：
           A  B  C
        a  1  4  7
        c  3  6  9
        ##############################
           A  B  C
        b  2  5  8
    iloc和loc的区别：1.iloc主要使用数字来索引数据，不能使用字符型的标签来索引数据。
                     2.loc只能使用字符型标签来索引数据，不能使用数字来索引数据。
                   特殊情况：当DataFrame的行标签或列标签为数组时，loc可以使用数字来索引。
"""

