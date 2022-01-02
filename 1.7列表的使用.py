# Python列表的使用
"""
    序列是Python中最基本的数据结构。序列中的每个元素都分配一个数
    字 - 它的位置，或索引，第一个索引是0，第二个索引是1，以此类推
    。Python有6个序列的内置类型，但最常见的是列表和元组。
    序列都可以进行的操作包括索引，切片，加，乘，检查成员。

    序列类型：元组，列表等。
"""
# 元组
"""
    元组是一种不可变序列，即创建之后不能再做任何修改。
    元组由不同的元素组成，每个元素可以存储不同类型的数据，如字符串、数字甚至元组。
    元组通常代表一行数据，而元组中的元素代表不同的数据项。
"""
# 元组的创建
"""
    格式：
        tuple=(元素1，元素2，... ,元素n)        # 定义n个元素组成的元组
        tuple=()                                # 定义空元组
        tuple=(元素1,)                          # 定义单元素元组
    例子：
        item = ('cat', -6, (1,2))
        print(item)
        print(type(item))
        print(item[0], item[1], item[2])
        item = ('cat')
        print(item)
        print(type(item))
        print(item[0])
        item = ('cat',)
        print(item)
        print(type(item))
        print(item[0])
        item = ()
        print(item)
        print(type(item))
        print(item[0])
    结果：
        ('cat', -6, (1, 2))
        <class 'tuple'>
        cat -6 (1, 2)
        cat
        <class 'str'>
        c
        ('cat',)
        <class 'tuple'>
        cat
        ()
        <class 'tuple'>
"""
# 元组的访问
"""
    元组中元素的值通过索引访问，索引是一对方括号中的数字，索引也称“下标”。
    格式：
        tuple[n]    # 访问第n个元素
        tuple[m:n]  # 访问第m个索引到底n个索引之间的索引元素，但不包括第n个索引指向的元素。
    其中，n、m可以为0、正、负整数。
    
    例子：
        fruit=('apple', 'banana', 'grape', 'orange')
        print(fruit[-1])
        print(fruit[-2])
        print(fruit[1:3])
        print(fruit[0:-2])
        print(fruit[2:-2])
        fruit1=('apple', 'banana')
        fruit2=('grape', 'orange')
        fruit=(fruit1, fruit2)
        print(fruit)
        print(fruit[0][1])
        print(fruit[1][1])
        print(fruit[1][2])
    结果：
        orange
        grape
        ('banana', 'grape')
        ('apple', 'banana')
        ()
        (('apple', 'banana'), ('grape', 'orange'))
        banana
        orange
        Traceback (most recent call last):
          File "D:/啥都有/Study/Python/1.7列表的使用.py", line 88, in <module>
            print(fruit[1][2])
        IndexError: tuple index out of range
    例子：操作元组
        t1 = (1, 'two', 3)
        t2 = (t1, 'four')
        print(t1+t2)
        print((t1+t2)[3])
        print((t1+t2)[2:5])
        print((t1+t2)[5])   # 错误，导致下方语句停止执行
        print((t1+t2)[4])   # four
        t3=('five',)
        print(t1+t2+t3)     # (1, 'two', 3, (1, 'two', 3), 'four', 'five')
    结果：
    (1, 'two', 3, (1, 'two', 3), 'four')
    (1, 'two', 3)
    (3, (1, 'two', 3), 'four')
    Traceback (most recent call last):
      File "D:/啥都有/Study/Python/1.7列表的使用.py", line 104, in <module>
        print((t1 + t2)[5])
    IndexError: tuple index out of range
    
    常用元组函数：
    函数名              返回值
    x in tupple         若x是元组tupple中的一个元素，则返回True，否则返回False
    len(tupple)         元组tupple包含的元素数
    tupple.count(x)     元素x在元组tupple中出现的次数
    tupple.index(x)     元组tupple中第一个元素x的索引，若x未包含在元组tupple中，将引发ValueError异常
    例子：
        pets = ('dog', 'cat', 'bird', 'dog')
        print(pets)
        for i in range(len(pets)):
            print(pets[i])
        print('bird' in pets)
        print('cow' in pets)
        print(pets.count('dog'))
        print(pets.index('dog'))
        print(pets.index('mouse')) 
    结果：
        Traceback (most recent call last):
          File "D:/啥都有/Study/Python/1.7列表的使用.py", line 131, in <module>
            print(pets.index('mouse'))
        ValueError: tuple.index(x): x not in tuple
        ('dog', 'cat', 'bird', 'dog')
        dog
        cat
        bird
        dog
        True
        False
        2
        0        
"""
# 列表
"""
    列表是Python中非常重要的数据类型，通常作为函数的返回类型。
    列表由一组元素组成。列表可包含任何类型的值：数字、字符串甚至
    序列。
    列表与元组的重要差别是列表是可变的，即可以在不复制的情况下添加、删除或修改元素。
"""
# 列表的创建
"""
    格式：
        list=[元素1,元素2,...,元素n]      # 定义n个元素组成的列表
        list=[]                           # 定义空列表
        list=[x]                          # 定义只包含一个元素的列表
    说明：列表用方括号括起，其中元素用逗号分隔。
    例子：
        numbers1 = [7, -7, 2, 3, 2]
        print(numbers1)
        print(type(numbers1))
        numbers2 = [7]
        print(numbers2)
        print(type(numbers2))
        numbers3 = []
        print(numbers3)
        print(type(numbers3))
    结果：
        [7, -7, 2, 3, 2]
        <class 'list'>
        [7]
        <class 'list'>
        []
        <class 'list'>
        
"""
# 列表的使用
"""
    列表的使用与元组十分相似，同样支持负数索引、分片以及多元列表等特性，但列表的元素可修改。
    与字符串和元祖一样，可使用len获取列表长度，还可以使用+和*拼接列表。
    例子：
        numbers = [7, -7, 2, 3, 2]
        print(numbers)
        print(numbers + numbers)
        print(numbers * 2)
        
        lst = [3, (1,), 'dog', 'cat']
        print(lst[0])
        print(lst[1])
        print(lst[2])
        print(lst[1:3])
        print(lst[2:])
        print(lst[-3:])
        print(lst[:-3])
        for i in range(len(lst)):
            print(lst[i], end = ' ')
    结果：
        [7, -7, 2, 3, 2]
        [7, -7, 2, 3, 2, 7, -7, 2, 3, 2]
        [7, -7, 2, 3, 2, 7, -7, 2, 3, 2]
        3
        (1,)
        dog
        [(1,), 'dog']
        ['dog', 'cat']
        [(1,), 'dog', 'cat']
        [3]
        3 (1,) dog cat 
    常用的列表函数
    函数名              返回值
    s.append(x)         在列表s末尾处添加元素x    
    s.count(x)          返回元素x在列表中出现的次数
    s.extend(lst)       将lst的所有元素都添加到列表s的末尾
    s.index(x)          返回第一个x元素的索引
    s.insert(i,x)       将元素x插入到索引i指定的元素前面，结果是s[i]=x
    s.pop(x)            删除并返回s中索引为x的元素
    s.remove(x)         删除s中的第一个x元素
    s.reverse()         翻转s中元素的排列顺序(将s的元素按降序排列)
    s.sort()            将s的元素按升序排列
    例子：
        lst = ['apple', 'banana', 'grape', 'orange']
        print(lst)
        lst.append('watermelon')
        print(lst)
        lst2 = ['strawberry', 'pear']
        print(lst2)
        lst.extend(lst2)
        print(lst)
    结果：
        ['apple', 'banana', 'grape', 'orange']
        ['apple', 'banana', 'grape', 'orange', 'watermelon']
        ['strawberry', 'pear']
        ['apple', 'banana', 'grape', 'orange', 'watermelon', 'strawberry', 'pear']
    例子：列表的查找、排序和反转
        lst = ['apple', 'banana', 'grape', 'orange']
        print(lst.index('grape'))
        print(lst.index('orange'))
        lst.sort()
        print('sorted list: ',lst)
        lst.reverse()
        print('reversed list: ',lst)
    结果：
        2
        3
        sorted list:  ['apple', 'banana', 'grape', 'orange']
        reversed list:  ['orange', 'grape', 'banana', 'apple']
    例子：给包含元组的列表排序
        pts = [(1,2), (1,-1), (3,5), (2,1)]
        print(pts)
        pts.sort()
        print(pts)
    结果：
        [(1, 2), (1, -1), (3, 5), (2, 1)]
        [(1, -1), (1, 2), (2, 1), (3, 5)]
    例子：用列表实现堆栈（“后进先出”的线性表）
        lst = ['apple', 'banana', 'grape']
        print(lst)
        lst.append('orange')
        print(lst)
        print('弹出的元素：', lst.pop())
        print(lst)
    结果：
        ['apple', 'banana', 'grape']
        ['apple', 'banana', 'grape', 'orange']
        弹出的元素： orange
        ['apple', 'banana', 'grape']
    例子：用列表实现队列（先进先出）
        lst = ['apple', 'banana', 'grape']
        print(lst)
        lst.append('orange')
        print(lst)
        print('队列的第一个元素：', lst.pop(0))
        print(lst)   
    结果：
        ['apple', 'banana', 'grape']
        ['apple', 'banana', 'grape', 'orange']
        队列的第一个元素： apple
        ['banana', 'grape', 'orange'] 
"""
