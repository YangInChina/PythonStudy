# 流程控制语句（下）
"""
    循环语句
        循环用于重复地执行代码块。
        Python中有两种主要的循环：
        for循环和while循环。
        for循环通常比while循环更容易使用。但没有while灵活
    break与continue
"""
# 循环语句
"""
    for循环
    格式：
        for 变量 in 集合：
        ...
    功能：每次从集合中取出一个值，并把值付给变量。集合可以是元组、列表、字典等数据结构。
    说明：for循环通常与range()函数一起使用，range（）函数返回一个列表，for循环遍历列表中的元素。
    range（）函数的格式：
        range（start,stop,[step]）
        参数start表示列表开始值，默认为0；
        参数stop表示列表结束值，不能缺省，循环到stop-1停止；
        参数step表示步长，默认值为1。
    例子：
        for i in range(10):
            print(i, " ", end="")
        print('')
        for i in range(5, 10):
            print(i, " ", end="")
        print('')
        for i in range(1,11):
            print(i, " ", end="")
        print('')
        for i in range(10):
            print(i + 1, " ", end="")
        print('')
        for i in range(10, 0, -1):
            print(i, " ", end="")
        print('')
        for i in range(10):
            print(10-i, " ", end="")
        print('')
    结果：
        0  1  2  3  4  5  6  7  8  9  
        5  6  7  8  9  
        1  2  3  4  5  6  7  8  9  10  
        1  2  3  4  5  6  7  8  9  10  
        10  9  8  7  6  5  4  3  2  1  
        10  9  8  7  6  5  4  3  2  1
    例子：求1+2+3+...+100
        s = 0
        for i in range(1,101):
            s += i
        print('sum =', s)
    结果：
        sum = 5050
    
    while循环
    格式：
    while 条件表达式：
        语句序列
    功能：当条件表达式为真时，依次执行while中的语句，直到循环表达式的值为假。
    例子：求1+2+3+...+100
        i = 1
        s = 0
        while i<=100:
            s += i
            i = i + 1
        print('sum =',s)
    结果:
        sum = 5050
        
    for循环和while循环比较
        固定次数的循环问题使用for循环和while循环都可以解决，
        循环次数不固定的循环问题只能使用while循环解决。
    例子：分别使用for循环和while循环计算n!
        n = int(input('Enter an integer >=0：'))         # for循环
        fact = 1
        for i in range(2, n + 1):
            fact = fact * i
        print(str(n) + "'s factorial is " + str(fact))
        n = int(input('Enter an integer >=0：'))         # while循环
        fact = 1
        i = 2
        while i <= n :
            fact = fact * i
            i = i + 1
        print(str(n) + "'s factorial is " + str(fact))
    结果：
        Enter an integer >=0: 5
        5's factorial is 120
    例子：计算已知个数数字的综合  使用for循环：
        n = int(input('How many numbers do you want to sun? : '))   # 使用for循环
        total = 0
        for i in range(n):
            s = input('Enter number ' + str(i + 1) + ': ')
            total = total + int(s）
        print('The sum is ' + str(total))
        n = int(input('How many numbers do you want to sun? : '))   # 使用while循环
        total = 0
        i = 1
        while i <= n :
            s = input('Enter number ' + str(i + 1) + ': ')
            total = total + int(s）
            i = i + 1
        print('The sum is ' + str(total))
    结果：
        How many numbers do you want to sun? : 5
        Enter number 1: 1
        Enter number 2: 2
        Enter number 3: 3
        Enter number 4: 4
        Enter number 5: 5
        The sum is 15
    例子：计算位置个数数字的总和。计算位置个数数字的总和就无法使用for循环完成了，只能使用while循环。
        s = input('Enter a number (or "done"): ')
        total = 0
        while s != 'done':
            num = int(s)
            total += num
            s = input('Enter a number (or "done"): ')
        print('The sum is ' + str(total))
    结果：
        Enter a number (or "done"): 4
        Enter a number (or "done"): 3
        Enter a number (or "done"): 5
        Enter a number (or "done"): 7
        Enter a number (or "done"): 4
        Enter a number (or "done"): done
        The sum is 23
    
    循环嵌套
    例子：输出九九乘法表。（for循环）
        for row in range(1,10):
            for col in range(1,10):
                prod = row * col
                if prod < 10:
                    print (' ', end='')
                print(row * col, ' ', end= '')
            print('')
    结果：
         1   2   3   4   5   6   7   8   9  
         2   4   6   8  10  12  14  16  18  
         3   6   9  12  15  18  21  24  27  
         4   8  12  16  20  24  28  32  36  
         5  10  15  20  25  30  35  40  45  
         6  12  18  24  30  36  42  48  54  
         7  14  21  28  35  42  49  56  63  
         8  16  24  32  40  48  56  64  72  
         9  18  27  36  45  54  63  72  81
"""
# break与continue语句
"""
    Python的跳转语句有：break语句和continue语句。以及类跳转语句。
    
    跳转语句的作用及区别：
        break语句的作用是：结束当前正在执行的循环（for、while）转而执行这些结构后面的语句。
                           结束整个循环，不再进行条件判断。
        continue语句的作用是：结束当前正在执行的这一次循环（for、while），接着执行下一次循环。
                              只结束本次循环，而不是终止整个循环的执行。
    例子：计算未知个数数字的总和（利用break语句）
        total = 0
        while True:
            s = input('Enter a number (or "done"): ')
            if s == 'done':
                break
            num = int(s）
            total += num
            print('The sun is ' + str(total))
    例子：输出1~100之间的不能被7整除的数。（利用continue语句）
        for i in range(1,101):
            if i % 7 == 0：
                continue
            print(i, ' ', end='')      
"""
