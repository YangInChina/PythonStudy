# 标识符
"""
    标识符由 字母、数字、下划线 组成
    所有标识符可以包括  英文、数字  以及  下划线（_)
    但不能以  数字  开头
    标识符区分大小写 如：A，a, _a, abc123 等
    以单下划线开头的标识符代表不能直接访问的“类”属性，需通过“类”提供的接口进行访问。
    以双下划线开头的标识符代表“类”的私有成员。
"""
# 保留字
# 写程序时，不能直接使用保留字作为常数或变数，或任何其他标识符名称。所有 Python 的关键字（保留字）只包括小写字母。
# 缩进与行
"""
    Python的代码块不适用大括号{}来控制“类”，函数以及其他逻辑判断。
    Python用缩进来写模块
    缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。
"""
# 正确示范
"""
   if True:    #True 开头大写
         print ("true")
   else:
         print ("false")
"""
# 错误示范
"""
         if True:    #True 开头大写
             print ("true")
         else:
             print ("false")
            print（"false")
"""
# 改正方法：用tab键或者空格缩进，与else对齐或者与print对齐（改为一致即可）
# 分号
""" Python的分号可以省略，主要通过换行来识别语句的结束。
    如果要在一行中书写多个语句，就必须适用分号。Python支持多行写一条语句，Python使用“\”（反斜杠）作为换行符。
      字符串换行举例：
      写法一：
        sql="select id,name\
        from dept\
        where name='A' "
        print (sql)
      写法二：
        sql="select id , name"\
        "from dept"\
        "where name = 'A' "
        print (sql)
    Python语法的特点：通常一行只写一条语句。
"""
# 引号
'''
    Python可以使用引号（')、双引号(")、三引号(''''''或"""""")来表示字符串，引号的开始与结束必须是相同类型的。
      如：
      word = 'word'
      sentence =  "这是一个句子。"
      paragraph = ''''''这是一个段落。''''''
      "包含多个句子。"
    其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。三引号可以是三个单引号
    也可以是三个双引号。
'''
# 注释
# Python中单行注释采用#开头
# Python中多行注释使用三个单引号或三个双引号
#    例子:
#    #这是单行注释
#    '''
#       这是多行注释，使用单引号
#       这是多行注释，使用单引号
#       这是多行注释，使用单引号
#    '''
#    """
#       这是多行注释，使用的双引号
#       这是多行注释，使用的双引号
#       这是多行注释，使用的双引号
#    """

# Python基础语法
'''
    print输出
    print 默认输出是换行的，如果要实现不换行需在变量末尾加上逗号
      x="a"
      y="b"
      #换行输出
      print(x)
      print(y)
      print('------')
      #不换行输出
      print (x, end=' ')
      print (y, end=' ')
      print (x,y)

      结果:
      a
      b
      ------
      a b a b
    print输入
    input可以接收一个Python表达式作为输入，并将结果返回。
    如：
       str=input("Please input a string:")
       print ("Your input is:" , str)
    结果：
    Please input a string:aaa
    Your input is: aaa
'''
# Python的变量类型
'''
    变量命名
      变量名的长度不受限制，其中的字符必须是字母、数字或下划线（_）
      变量名的第一个字符不能是数字，必须是字母或者下划线。
      变量名中不能使用空格，标点符号，连字符，引号或者其他字符
      Python区分大小写，因此TAXTax和tax是截然不同的变量
      不能将Python关键字（或称为保留字）用作变量名，例如：if、else、while、def、or、and、not、in和is都是Python关键字
    变量赋值
      每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
      每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
      等号（=）用来给变量赋值
      等号（=）运算符左边是一个变量名，右边是存储在变量中的值。
        如：counter = 100 #整形
            miles = 1000.0 #浮点型
            names = "John" #字符型
    多重赋值
      如：x,y,z = 1 , 'two' , 3.0
    局部变量和全局变量

      局部变量是只能在函数或代码块内使用的变量。
      函数或代码一旦结束，局部变量的生命周期也就结束
      局部变量的作用只能在其被创建的函数内有效
        如：def fun():
            local = 1
            print(local)

            fun()
            print(local) #此时已经超出了local变量的作用范围，会报错
        结果：NameError: name'local' is not defined

      全局变量是能够被不同的函数、类或文件共享的变量。
      在函数之外定义的变量都可以成为全局变量。
      全局变量可以被文件内部任何函数和外部文件访问。
      通常约定俗成将全局变量放在文件头。
        如: _a = 1
            _b = 2
            def add():
                global _a    #用global引用全局变量
                _a = 3       #给全局变量_a重新赋值
                return "_a + _b =" , _a + _b

            def sub():
                global _b
                _b = 4
                return "_a - _b = ", _a - _b

            print (add())
            print (sub())
        结果：('_a + _b =', 5)
              ('_a - _b =', -1)
    数据类型
      Python有几种内置的数据类型：
      数字（numbers）
            Python 3的数字类型分为：整型、浮点型、布尔型、复数类型
            如：i = 1
                print(type(i))
                l = 9999999999999999999999
                print(type(l))
                f = 1.2
                print(type(f))
                b = True
                print(type(b))
                c = 7 + 8j
                print(type(c))
            结果：
                <class 'int'>
                <class 'int'>
                <class 'float'>
                <class 'bool'>
                <class 'complex'>
      字符串（string）
            Python中，可以使用三种方式表示字符串。
            单引号，双引号和三引号
            string输出用print（）
      元组(tuple)
      列表(list)
      字典(dictionary)
'''
