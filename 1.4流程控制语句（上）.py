# 流程控制语句（上）
"""
    if-elif-else的使用
    if嵌套的使用
"""
# if-else语句（单分支）
"""
    例如：
        a = input("a:")
        a = int(a)
        if(a > 0):
            print(a,"是正数")
"""
# if-else语句（多分支）
"""
    格式：
        if(表达式):
            语句序列1
        else：
            语句序列2
"""
# if...elif...else语句
"""
    if/elif语句是if语句的扩展版本，它包含多个条件，用于做出复杂的决策
        例：假如航空公司提供了儿童优惠票价：不超过2岁的儿童免票；2-13岁的儿童打折；13岁以上儿童与成人同价。
            age = int(input("How old are you?"))
            if age <= 2 :
                print('free')
            elif 2<age<13:
                print('child fare')
            else:
                print('adult fare')
        结果：
            How old are you?:2      # 第一次测试
            free
            How old are you?:7      # 第二次测试
            child fare
            How old are you?:16     # 第三次测试
            adult fare      
"""
# if嵌套的使用
"""
    if 语句内还可以使用if语句，这样就构成了if语句的嵌套。
    格式：
        if(表达式1)；
            if(表达式1.1):语句序列1.1
            elif(表达式1.2):语句序列2.2
            ...
        elif(表达式2):语句序列2
        elif(表达式n):语句序列n
            ...
        else:
            ...
    例子：输入三个数，输出最大数
        a = int(input('input a:'))
        b = int(input('input b:'))
        c = int(input('input c:'))
        if a < b:
            if b < c:
                max = c
            else:
                max = b
        else:
            if a<c :
                max = c
            else :
                max = a
        print('max =',max)
    结果：
        input a:2
        input b:5
        input c:1
        max = 5
"""
# 条件表达式
"""
    Python也有类似于C++的条件表达式：条件表达式也称为三元表达式
        表达式的形式：x if C else y
        流程是：如果c为真，那么执行x，否则执行y。
    例子：
        a = int(input('input a:'))
        b = int(input('input b:'))
        max = a if a>b else b
        print('max =',max)
    结果：
        input a:2       # 第一次测试
        input b:5
        max = 5
        input a:2       # 第二次测试
        input b:5
        max = 5
"""