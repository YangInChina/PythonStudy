# 字符串
"""
    在Python中，字符串是除数字外最终要的数据类型。字符串无处不在：将字符串输出到屏幕上；从用户的键盘
输入读取字符串；文件通常被视为大型字符串；网页大部分是由文本组成的。
    字符串是一种聚合数据结构，可充分利用索引和切片——用于从字符串中提取子串。
    而Python正则表达式库，是一种用来处理字符串的微型语言，但功能强大。
    Python中，字符串、列表和元组都属于序列。
    序列有一些通用操作。包括：索引（indexing）、分片（slicing）、加【连接】（adding）、乘（multiplying）、
检查某个元素是否属于序列的成员（成员资格）、计算序列长度、找出最大元素和最小元素等。
    字符串的常见操作：字符串格式化
"""
# 索引
"""
    序列中的所有元素都是有编号的——从0开始递增。这些元素可以通过编号分别访问。索引有正索引和负索引，可根据实际情况选用。
    字符串就是一个由字符组成的序列，处理字符串时，经常需要访问其中的各个字符。索引0指向第一个字符。
    例子：字符串'apple'的正索引和负索引
        s = 'apple'
        则，正索引与C++一致，s[0]==a ; s[1]==p ; s[2]==p ; s[3]==l; s[4]==e
        而负索引的对应关系为：s[-5]==a ; s[-4]==p ; s[-3]==p ; s[-2]==l ; s[-1]==e
    例子：字符串索引应用
        s = 'apple'
        for i in range(len(s)) :             # len()函数求字符串长度
            print(s[i], end = '')
        print()
        for i in range(len(s)) :
            print(s[-(i+1)], end = '')
    结果：
        apple
        elppa
    例子：计算给定字符串的编码总和。
        def codesum(s)：                     # return the sum of the character codes of s.
            total = 0
            for c in s :
            total = total + ord(c)           # ord()函数获取字符的Unicode编码，该编码的钱256个字符位ASCII码
            return total
        print(codesum('Hi there!'))
    结果：
        72
"""
# 分片
"""
    与使用索引访问单个元素类似，可以使用分片操作来访问一定范围内的元素。分片是实际应用中经常
使用的技术，被截取的部分称为“子串”
    Python 3支持的分片格式为：
        S[i:j:k] i缺省值为0，j缺省值为len(S),k缺省值为1
        表示：索引S对象中的元素，从索引为i直到索引为j-1，每隔k个元素索引一次，第三个限制k为步长，默认值为1.
        在Python中，还可以使用split()函数来截取字符串。
    例子：
        food = 'apple pie'
        print(food[0:5])
        print(food[6:9])
        print(food[:5])
        print(food[6:])
        print(food[-9:-4])
        print(food[:-4])
        print(food[-3:0])# 最后一个字符e对应倒叙为food[-1],而food[0]=='a'==food[-9],从-3到-9在步长为1的条件下无法执行。结果为空。
        print(food[-3:-1])# -1的确存在，但该切片不包括它，所以结果是pi
        print(food[-3:])
        print(food[::2])
        print(food[1::2])
        print(food[::-1])
    结果：
        apple
        pie
        apple
        pie
        apple
        apple
        
        pi
        pie
        apepe
        pl i
        eip elppa
"""
# 序列相加(字符串连接、合并)
"""
    例子：
        print('Hello,' + 'world!')
    结果：
        Hello,world!
        
    除可以使用“+”完成之外，还可以使用join函数和reduce函数实现字符串的合并。
    注意：不同类型的数据不能相加。
"""
# 乘法
"""
    用数字x乘以一个序列会生成新的序列，在新的序列中，原来的序列被重复x次。6
    例子：
        print（'Python ' * 5）
    结果:
        Python Python Python Python Python 
"""
# 成员资格
"""
    为了检查一个值是否在序列中，可以使用in运算符，若为真返回Ture，否则返回False。
    例子：
        permissions = 'rw'
        print('w' in permissions)
        print('x' in permissions)
    结果：
        True
        False
"""
# 长度、最小值和最大值
"""
    len、min和max都是内置函数。
    len——返回序列中包含的元素个数。
    min——返回序列中的最小值。
    max——返回序列中的最大值。
    例子：
        print(len('Hello world'))
        print(max('bcd','fig','abcd','xyz','abab'))
        print(min('bcd','fig','abcd','xyz','abab'))
    结果：
        11
        xyz
        abab
"""
# 字符串的格式化
"""
    C语言使用函数printf（）格式化输出结果，Python也提供了类似的功能。
    Python将若干值插入带有“%”标记得字符串中，从而可以按照指定格式输出字符串。
    语法：
        "%s"%str1
        "%s%s"%(str1,str2)
    例子：
        str1 = 'version'
        num = 1.0
        format = '%s' % str1
        print(format)
        format = '%s %d' % (str1, num)
        print(format)
    结果：
        version
        version 1

    Python格式化字符串的替代符及含义
    符号  描述
    %c    格式化字符及其ASCII码
    %s    格式化字符串
    %d    格式化整数
    %u    格式化无符号整数
    %o    格式化无符号八进制数
    %x    格式化无符号十六进制数
    %X    格式化无符号十六进制数（大写）
    %f    格式化浮点数字，可指定小数点后的精度
    %e    用科学计数法格式化浮点数
    %E    作用同%e
    %g    根据值的大小决定使用%f或%g
    %G    作用同%g
    %p    用十六进制格式化变量的地址
    %%    若在字符串中输出“%”，需要使用“%%”
"""
# 字符串的转义字符
"""
    计算机中存在可见字符与不可见字符。可见字符指键盘上的字母、数字和符号。不可见字符是指换行、回车、制表符等字符。
    对于不可见字符，Python使用方法类似于C语言，都是使用“\”作为转义字符。
    Python还提供了函数strip()、Istrip()、rstrip去除字符串中的转义字符。
    Python常用的转义字符及其含义：
    符号    描述
    \\      反斜杠
    \'      单引号
    \"      双引号
    \a      发出系统响铃声
    \b      退格符
    \n      换行符
    \t      横向制表符
    \v      纵向制表符
    \r      回车符
    \f      换页符
    \o      八进制代表的字符
    \ x     十六进制代表的字符
    \000    终止符，其后的字符串全部忽略
    例子：
        print（'\' and \" are quotes'）
        print('\\ must be written \\\\')
        print('one\ntwo\nthree')
        print(r'hello\tworld\n')            # 忽略转义符作用，直接输出字符串原始内容
        print（len('\\')）                  # 计算字符串长度时，不包括转义符
        print(len('a\nb\nc'))               # 计算字符串长度时，不包括转义符
    结果：
        ' and " are quotes
        \ must be written \\
        one
        two
        three
        hello\tworld\n
        1
        5
"""
# 字符串函数
"""
    Python字符串自带了大量很有用的函数，要查看这些函数，可调用dir并将参数指定为任何字符串(如：dir(''))。
    虽无必要准确记住所有函数功能，但最好有个大致了解，这样有益于需要时去查询具体使用。
    字符串函数的消息介绍可参阅其文档字符串或Python在线文档(https://docs.python.org/3/)
    测试函数：
        用于检测字符串是否为特定格式的函数，它们组成了一个最大的字符串函数组。
        测试函数都返回True或False，因此也称为布尔函数或谓词。
    函数名              何时返回True
    s.endswith(t)       s以字符串t结尾
    s.startswith(t)     s以字符串t打头
    s.isalnum()         s只包含字母和数字
    s.isalpha()         s只包含字母
    s.isdecimal()       s只包含表示十进制数字和字符
    s.isdigit()         s只包含数字字符
    s.isidentifier()    s是合法的标识符
    s.islower()         s只包含小写字母
    s.isnumber()        s只包含数字
    s.isprintable()     s只包含可打印字符
    s.isspace()         s只包含空白字符
    s.istitle()         s是个大小写符合标题要求的字符串
    s.isupper()         s只包含大写字母
    t in s              s包含字符串t
    例子：
        s = 'Hello world!'
        print(s.startswith('h'))
        print(s.endswith('!'))
        print(s.islower())
        print(s.isupper())
        print(s.isprintable())
    结果：
        False       # 第一个元素是“H”而不是“h”
        True
        False
        False
        True
    
    函数名          返回值
    s.find(t)       若未找到字符串t,则返回-1;否则返回t在s中的起始位置
    s.rfind(t)      与find相同，但从右往左查找
    s.index(t)      与find相同，但如果在s中找不到t,则引发ValueError异常
    s.rindex(t)     与index相同，但从右往左查找
    例子：
        s = 'cheese'
        print(s.find('e'))
        print(s.index('e'))
        print(s.rfind('e'))
        print(s.find('eee'))
        print(s.index('eee'))
    结果：
        2
        2
        5
        -1
        Traceback (most recent call last):
          File "D:/啥都有/Study/Python/1.6Python字符串的使用.py", line 248, in <module>
            print(s.index('eee'))
        ValueError: substring not found
    函数名                  返回值
    s.replace(old,new)      将s中的每个old替换为new
    s.expandtabs(n)         将s中的每个制表符扩展为空格，空格宽度为n
    例子：
        s = 'up, up and away'
        s1 = 'up, \tup\tand\taway'
        print(s.replace('up', 'down'))
        print(s.replace('up', ' '))
        print(s1)
        print(s1.expandtabs(8))
        print(s1.expandtabs(10))
    结果：
        down, down and away
         ,   and away
        up, 	up	and	away
        up,     up      and     away
        up,       up        and       away
    
    合并：
        之前介绍过，Python可使用“+”连接不同的字符串。
        除此之外，还可以使用join函数（是split方法的逆方法）和reduce函数实现字符串的合并
        例子：
            strs = ['hello', 'world', 'hello', 'China']
            result = ' '.join(strs)
            print(result)
            seq = ['1', '2', '3', '4', '5']
            sep = '+'
            print(sep,join(seq))
        结果：
            hello world hello China
            1+2+3+4+5
        
    函数名           返回的字符串
    s.partition(t)   将S拆分为三个字符串（head、t和tail），其中head为t前面的子串，tail为t后面的子串。返回值为元组。
    s.rpartition(t)  与partition相同，但从s的右端开始搜索t。返回值为元组。
    s.split(t)       以t为分隔符，将s划分成一系列子串，并返回一个由这些字串组成的列表
    s.rsplit(t)      与split相同，但从S的右端开始搜索t
    s.splitlines()   返回一个由s中的各行组成的列表
    例子：
        url = 'www.google.com'
        print(url.partition('.'))
        print(url.rpartition('.'))
        print(url.split('.'))
        story = 'A long time ago, a princess ate an apple'
        print(story.split())
    结果：
        ('www', '.', 'google.com')
        ('www.google', '.', 'com')
        ['www', 'google', 'com']
        ['A', 'long', 'time', 'ago,', 'a', 'princess', 'ate', 'an', 'apple']
    例子：使用split()函数获取子串
        sentence = 'Bob said: 1, 2, 3, 4,'
        print('使用空格抓取子串'， sentence.split())
        print('使用逗号抓取子串'， sentence.split(','))
        print('使用两个逗号抓取子串'， sentence.split(',', 2))
    结果:
        使用空格抓取子串 ['Bob', 'said:', '1,', '2,', '3,', '4']
        使用逗号抓取子串 ['Bob said: 1', ' 2', ' 3', ' 4']
        使用两个逗号抓取子串 ['Bob said: 1', ' 2', ' 3, 4']
        
    字符串的比较
        Python直接使用“==”、“！=”操作符比较两个字符串的内容。如果比较的两个变量的类型不相同、比较的内容
    也不相同。
        若要比较字符串的部分内容，可以衔接去子串，再使用“==” “!=”操作符进行比较。
    例子：
        str1 = 1
        str2 = '1'
        str3 = 2
        if str1 == str2:
            print('same')
        else:
            print('different')
        if str(str1) == str2:
            print('same')
        else:
            print('different')
        if str(str3) == str2:
            print('same')
        else:
            print('different')
    结果：
        different
        same
        different
"""