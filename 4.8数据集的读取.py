# 数据集的读取
"""
    pandas读取CSV文件
    pandas读取Excel文件
"""
# pandas读取CSV文件
"""
    pandas提供了一个非常简单的函数read_csv()来实现把存储在csv格
式中的数据读入并转换成DataFrame格式的功能。
    函数read_csv()基本格式：
    pandas.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None,
                    index_col=None, usecols=None, nrows=None,...)
    filepath_or_buffer:任何有效的字符串路径（即文件路径）。文件路径包括csv文件的绝
对路径、相对路径和URL，如本地的文件路径就可以写成：file://localhost/path/to/table.csv
    sep：指定分隔符。一般csv默认逗号为分隔符，如果想使用其他字符串对
csv文件进行分隔，可以指定为其他字符。
    delimiter：定界符，备选分隔符（如果指定该参数，则sep无效），默认
为None。sep的别名。
    header：指定DataFrame的某行为列标签，默认为第一行，等同于header=0.
如果header=1，则第二行选为列标签。特别地，如果header=None，则列名为0,1,2,3...
如果设置header=[0,1,2]，则将0,1,2中的值组合为列名。
    注意：header=0表示数据的第一行而不是文件的第一行，因为有时会跳过空白行，
此时header=0不会指定跳过的空白行为列标签。
    names：用于结果的列名列表，默认为None。如果数据文件中没有列标
题行，就需要执行header=None。
    usecols：可以选择想要返回的列，可以按列读取，也可以按列名取。
    nrows：需要读取的行数（从文件头开始算起）。

"""