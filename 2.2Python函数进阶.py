# Python函数进阶
"""
    局部变量和全局变量
    匿名函数，递归函数
"""
# 局部变量
"""
    局部变量是只能在函数或代码块内使用的变量。
    函数或代码块一旦结束，局部变量的生命周期也就结束。
    局部变量的作用范围只在其被创建的函数内有效。

    例子：
        def fun():
            local = 1
            print(local)
        fun()
        print(local)
    结果：
        Traceback (most recent call last):
          File "D:/啥都有/Study/Python/2.2Python函数进阶.py", line 20, in <module>
            print(local)
        NameError: name 'local' is not defined
        1    
"""
# 全局变量
"""
    1.全局变量是能够被不同的函数、类或者文件共享的变量。
    2.在函数之外定义的变量都可以称为全局变量。
    3.全局变量可以被文件内部的任何函数和外部文件访问。
    4.全局变量通常在文件的开始处定义。
    例子：
        _a = 1
        _b = 2
        def add():
            global _a
            _a = 3
            return '_a + _b= ', _a + _b
        def sub():
            global _b
            _b = 4
            return '_a - _b= ', _a - _b
        print(add())
        print(sub())
    结果：
        ('_a + _b= ', 5)
        ('_a - _b= ', -1)

    慎用全局变量
        1.应该尽量避免使用全局变量。因为不同的模块都可自由地访问全局变量，可能
        会导致全局变量的不可预知性。
        2.对于上例中gl.py中的全局变量，若程序员甲修改了_a的值，程序员乙同时也要
        使用_a，此时就可能导致程序的错误。这种错误是很难发现和更正的。
        3.全局变量降低了函数或模块之间的通用性，不同的函数或模块都要依赖于全局变
        量。同样，全局变量降低了代码地可读性，阅读程序者并不知道调用的某个变量
        是全局变量。
"""
# 匿名函数
"""
    Lambda函数用于创建一个匿名函数，函数名未和标识符进行绑定。
    使用Lambda函数可以返回一些简单的运算结果。
    格式：Lambda 变量1，变量2...：表达式
    功能：通常Lambda赋值给一个变量，变量即可作为函数使用；也可以把Lambda直接
    作为函数使用。
    例子：
        def fun():
            x = 1
            y = 2
            m = 3
            n = 4
            sum = lambda x, y: x + y  # 将Lambda和变量sum绑定在一起，变量sum的名称就是函数名
            print(sum)
            sub = lambda m, n: m - n
            print(sub)
            return sum(x, y) + sub(m, n)
        print(fun())
    结果：
        <function fun.<locals>.<lambda> at 0x00000234B43FCC10>
        <function fun.<locals>.<lambda> at 0x00000234B43FCCA0>     
        2
    例子：使用Lambda定义求相反数的匿名函数。
        print((lambda x: -x)(-2))       # 定义了匿名函数lambda x:-x,用于返回数字的绝对值。
    结果：
        2
"""
# 递归函数
"""
    递归函数可以再函数主题内直接或间接地调用自己，即函数的嵌套是函数本身。
    递归函数是一种程序设计方法，使用递归可以减少重复地代码，使程序变得简洁。
    递归过程分为两个阶段：递推和回归。
    
    注意：
        一个问题能否用递归实现，看其是否具有以下的特点：
        1.需有完成任务的递推公式。
        2.结束递归的条件。
        编写递归函数时，程序中必须有相应的语句：
        一个递归调用语句。
        测试结束语句。先测试，后递归调用。
        
    例子：
        def f(n):
            if n == 1:
                return 1
            else:
                return n * f(n - 1)
        n = int(input('请输入阶乘数：'))
        print(str(n) + '的阶乘为: ', f(n))
    结果：
        请输入阶乘数：5
        5的阶乘为:  120
    例子：编程求出Fibonnacci数列的第n项（假定求出第八项）
    分析：Fibonnacci数列的计算具备递归的条件。首先有递归公式F(n) = f(n-1) + f(n-2)
          第二有结束递归的条件，即n=0或n=1时不再递归。
        def fibo(n):
            if n == 1 or n == 2:
                return 1
            else:
                return fibo(n - 1) + fibo(n - 2)
        print(fibo(n=int(input('请输入要求第几项：'))))
    结果：
        请输入要求第几项：8
        21        
"""