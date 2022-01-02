# Python函数的使用
"""
    函数的介绍
    函数的基本使用
"""
# 函数的介绍
"""
    Python的程序由包、模块和函数组成。
    函数是一段可重复利用的有名称的代码。通过输入参数值，返回
    需要的结果，并可存储在文件中供以后使用。几乎任何Python代码
    都可以放在函数中。Python为函数提供了强大的支持。
    
    模块是处理某一类问题的集合，模块由函数和类组成。
    模块和常规Python程序之间的唯一区别是用途不同：模块用于编写
    其他程序。因此，模块通常没有main函数。
    
    包是一个完成特定任务的工具箱，Python提供了许多有用的工具包，如
    字符串处理、图形用户接口、Web应用、图像处理等。使用自带的工具包，
    可以提高程序开发效率、减少编程复杂度，达到代码重用的效果。
    
    Python自带的工具包和模块安装在其安装目录的Lib子目录中
    例子：
        xml文件夹就是一个包，该包用于完成XML的应用开发，xml包中包含四个子包：dom、sax、
        etree和parsers。文件__init__.py是xml包的注册文件，若无此文件，Python将不能识别
        xml包。
    注意：
        包必须至少含有一个__init__.py文件。__init__.py文件的内容可以为空，它用于标识
        当前文件夹是一个包。
"""
# 可更改对象（mutable）与不可（immutable）更改对象
"""
    在Python中，strings, tuples 和 numbers 是不可更改的对象，而list, dict等
    则是可更改的对象。

    不可变类型：变量赋值 a=5 后再赋值 a=10, 这里实际是新生成一个 int 值对象 10，
    再让 a 指向它， 而5被丢弃， 不是更改a的值，相当于新生成了a。
    可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将list la 的第三个元素值
    更改，本身la没有动，只是其内部的一部分值被修改了。
"""
# 函数的定义及调用
"""
    函数定义：
    格式：
        def 函数名(形参表):
            函数体语句序列
            [return 表达式]    # 可选项，即有的函数可以没有返回值。
    
    
    函数调用：
        函数名(实参表)
    注意：
        函数必须先定义，后使用；
        函数名与变量名的命名规则相同，只能包含字母、数字和下划线_，
        且不能以数字打头。
    例：计算圆的面积
        import math
        def area(radius):
            return math.pi * radius ** 2
        print(area(5.5))
        print(2 * (area(3) + area(4)))
    结果：
        95.03317777109125
        157.07963267948966
    
    
    函数的参数：
    在C、C++中，参数的传递有值传递和引用传递两种方式。Python
    中任何东西都是对象，所以参数只支持引用传递的方式。
    Python通过名称绑定的机制，把实际参数的值和形式参数的名称
    绑定在一起，即把形式参数传递到函数所在的局部命名空间中，
    形式参数和实际参数指向内存中同一存储空间。
    例子：求任意两个数的和
        def add(a, b):
            return a + b
        x, y = 3, 4
        print(x, '+', y, '=', add(x, y))        
    结果：
        3 + 4 = 7
    内存状态：
        将x和y分别设置为3和4的内存状态：
        x————>3
        y————>4
        
        刚调用add(a, b)后的内存状态，a和b分别指向x和y指向的值。
        x————>3<————a
        y————>4<————b
        
    Python函数的参数传递：
    不可变类型：类似C++的值传递，如 整数、字符串、元组。如fun(a),传递
    的只是a的值，没有影响a对象本身。比如在fun(a)内部修改a的值，只是修
    改另一个复制的对象，不会影响a本身。
    可变类型：类似C++的引用传递，如 列表、字典。如fun(la)，则是将la真正
    的传过去，修改后fun外部的la 也会受到影响。
    
    默认值：函数的参数支持默认值。当某个参数没有传递实际的值时，函数将使用默认
    参数计算。带默认值的参数不能位于没有默认值的参数前面。
    例子：
        def greet(name, greeting='Hello'):
            print(greeting, name + '!')        
        greet('Bob')
        greet("Bob", 'Good morning')
    结果：
        Hello Bob!
        Good morning Bob!
    
    关键字参数：关键字参数有两大好处：
        清晰地指出了参数值，有助于提高程序的可读性；
        关键字参数的顺序无关紧要。
    调用使用关键字参数的函数时，以param=value的方式传递参数。
    例子：
        def shop(where='store', what='pasta', howmuch='10 pounds'):
            print('I want you to go to the', where)
            print('and buy', howmuch, 'of', what + '.')
        
        
        shop()
        shop(what='towels')
        shop(howmuch='a ton', what='towels')
        shop(howmuch='a ton', what='towels', where='bakery')  
    结果：
        I want you to go to the store
        and buy 10 pounds of pasta.
        I want you to go to the store
        and buy 10 pounds of towels.
        I want you to go to the store
        and buy a ton of towels.
        I want you to go to the bakery
        and buy a ton of towels.
    
    函数的嵌套：
        C、C++都支持函数的嵌套调用，Python不仅支持函数的嵌套调用，
        还支持函数的嵌套定义。
        当然，尽量不要在函数内部定义函数，这种方式不便于程序维护，
        容易造成逻辑上的混乱，且嵌套定义的函数层数越多，程序维护的
        代价越大
    例子：分别使用函数的嵌套调用、函数的嵌套定义以及函数嵌套定义时
          直接引用外部函数的变量等三种方式，计算表达式(x+y)*(m-n)的值
        def sum(a, b):
            return a + b
        def sub(a, b):
            return a - b
        def func():
            x = 1
            y = 2
            m = 3
            n = 4
            return sum(x, y) * sub(m, n)        # 函数的嵌套调用
        print(func())
    结果：
        -3
        def func():                             # 函数的嵌套定义
            x = 1
            y = 2
            m = 3
            n = 4
            def sum(a, b):
                return a + b
            def sub(a, b):
                return a - b
            return sum(x,y)*sub(m,n)
        print(func())        
    结果：
        -3
        def func():                             # 函数嵌套定义，内部函数直接引用外部函数的变量
            x = 1
            y = 2
            m = 3
            n = 4
            def sum():
                return x + y
            def sub():
                return m - n
            return sum()*sub()
        print(func()) 
    结果：
        -3
"""