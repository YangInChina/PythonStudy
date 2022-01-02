# 异常与模块
# 异常
"""
    异常即是一个事件，该事件会在程序执行过程中发生，影响程序的正常执行。
    当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。

    异常举例：
    IOError：输入/输出操作失败
    SystemExit：解释器请求退出
    KeyboardInterrupt：用户中断执行（通常是输入^c）
    Exception：常规错误的基类
    StopIteration：迭代器没有更多的值
    GeneratorExit:生成器（Generator）发生异常来通知退出
    StandardError：所有的内建标准异常的基类
    ArithmeticError：所有数值计算错误的基类
    FloatingPointError：浮点数计算错误
    OverflowError：数值运算超出最大限制
    ...

    捕捉异常可以使用try/except语句。
    try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。
    以下为简单的try...except...else的语法：
    try:
        <code>
    except  <name>,<data>:
        <code>
    else:
        <code>
    try的工作原理是，当开始一个try语句后，Python就在当前程序的上下文中
    做标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生
    什么依赖于执行时是否出现异常。
    如果当try后的语句发生异常，Python就跳回到try并执行第一个匹
    配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非
    在处理异常时又引发新的异常）。
    如果在try后的语句里发生了异常，却没有匹配的except子句，异常
    将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印
    缺省的出错信息）。
    如果在try子句执行时没有发生异常，Python将执行else语句后的语句
    （如果有else的话），然后控制流通过整个try语句。

    例子：
        try:
            fh = open('testfile','w')
            fh.write('This is a testfile')
        except IOError:
            print('Error')
        else:
            print('Done')
            fh.close()
    结果：
        Done
"""
# 模块
"""
    模块实际上是将一组函数放在一起共享公共的主题；
    将这些函数存储于一个.py文件中；
    使用import命令导入。
    
    模块的创建及导入：
    创建模块即创建一个.py文件，在其中包含用于完成任务的变量、类、和函数，不包括main函数。
    模块使用之前要导入该模块，导入方法之前已做过介绍。
    
    例子：创建模块，用于在屏幕上打印各种形状。
        import shapes
        
        print(dir(shapes))  # 将shape里方法和函数输出
        
        print(shapes.__doc__)
        print()
        
        print(shapes.CHAR)
        print()
        
        shapes.square(5)
        print()
        
        shapes.triangle(3)
        print()
        
        shapes.rectangle(3, 8)
        print()
    结果：
        ['CHAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'rectangle', 'square', 'triangle']
        None
        
        *
        
        *****
        *****
        *****
        *****
        *****
        
        *
        **
        ***
        
        ********
        ********
        ********
    例子：创建一个求圆面积、圆周长、圆表面积和球体积的模块。
        import RingandBall
        pi = 3.0
        print(pi)
        print(RingandBall.pi)
        print(RingandBall.area(3))
        print(RingandBall.circunference(3))
    结果：
        3.0
        3.14159
        28.27431
        18.849539999999998
    调用方式二：
        from RingandBall import *   # 引进所有函数
        
        pi = 3.0
        print(pi)
        print(pi)
        print(area(3))
        print(circunference(3))
    结果：
        3.0
        3.0
        28.27431
        18.849539999999998
        
    模块的属性及导入：
        模块有一席内置属性，用于完成特定的任务。
        如：
            __doc__：模块中用于描述的文档字符串
            __name__：模块名
            __file__：模块保存的路径
    模块的内置函数：
        Python提供了一个内联模块buildin。
        该模块定义了一些常用函数，利用这些函数可以实现数据类型的转换、数据的计算、序列的处理等功能。
    如：reduce()
    声明：
        reduce(func,squence[,initial]->value)
    功能：对序列中的元素进行连续的操作。
    例如：可对某个序列中的元素进行累加、累乘和阶乘等操作。
    说明：在Python2中，reduce存在于全局空间中，可直接调用。而在Python3中将
    其移到了functools模块中，所以使用前要引入。
    
    例子：
        def sum(x, y):
            return x + y
        
        
        from functools import reduce
        
        print(reduce(sum, range(0, 10)))    # 0+1的结果再和2加，结果再和3加，实质上是[0,10]进行累加，结果为45
        print(reduce(sum, range(0, 10), 10))    # 10为初始值,10+0,结果再加1，实质上是10+[0,10]的累加，结果为55
        print(reduce(sum, range(0, 0), 10))     # 10位初始值，实际上是10+[0,0]的累加，结果为10
    结果：
    45
    55
    10
    
    如：
    map()
    声明：
        class map(object)
            map(func,iterables)->map object
    功能：对多个序列的每个元素都执行相同的操作，并返回一个map对象。    
    例子：
        def power(x):
            return x ** x
        
        
        print(map(power, range(1, 5)))  # 打印map对象
        print(list(map(power, range(1, 5))))  # 转换为列表输出
        
        
        def power2(x, y):
            return x ** y
        
        
        print(map(power2, range(1, 5), range(5, 1, -1)))  # 前一个range是x的实参，后一个range是y的实参。
        print(list(map(power2, range(1, 5), range(5, 1, -1))))
    结果：
        <map object at 0x0000016D82007B80>
        [1, 4, 27, 256]
        <map object at 0x0000016D8201F700>
        [1, 16, 27, 16]
        
    常用内置模块函数：
    abs(x)：返回x的绝对值
    bool([x])：将一个值或者表达式转换为bool类型。如果表达式x为真，返回True，假，则返回False。
    delatrr(obj.name)：等价于del obj.name
    eval(s[,globals,locals])：计算表达式的值
    float(x)：将数字或者字符串转换为float类型。
    hash(object)：返回一个对象的hash值。
    help([object])：返回内联函数的帮助说明。
    id(x)：返回一个对象的标识。
    input([prompt]):接受控制台的输入，并将输入的值转换为字符串（Python3）
    int(x)：将数字或者字符串转换为整型。
    len(obj)：对象包含的元素个数。
    range([start],end,[step])：生成一个列表并返回。
    reduce(func,sequence[initial])：对序列的值进行累计计算。
    round(x,n=0)：四舍五入函数。
    set([iterable])：返回一个set集合。
    sorted(iterable[,cmp[,key[,reverse]]])：返回排列后的列表。
    type(obj)：返回一个对象的类型。
    zip(iter1[,iter2[...]])：将n个序列作为列表的元素返回。
"""



