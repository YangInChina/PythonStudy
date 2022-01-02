# Python字典与集合
"""
    字典：字典是Python重要的数据类型，字典是由“键——值”对组成的集合，
          字典中的“值”通过“键”来引用。
          字典也称关键数组、映射或散列表。
          Python字典利用了“散列”方法，使用专门的散列函数完成，即字
          典中的每个键都被转换为一个数字——散列值。字典中值存储在一个底
          层列表中，并用散列值作为索引。访问值时，将提供的键转为散列值
          ，再跳到列表的相应位置。
          使用“键”来访问字典值效率极高。另外与列表一样，字典也是可以改
          变的：可以添加、删除或修改“键——值”对。
"""
# 创建字典
"""
    格式：
        dictionary={key1:value1, key2:value2,...,keyn:valuen}   #创建n个“键——值”对组成的字典
        dictionary={}                       # 创建空字典
    注意：对于字典的键有两个限制：
        字典中的键必须独一无二，即在同一个字典中，任何两个键——值对都不能相同。
        值可以取任何数据类型，必须是不可变的，如字符串，数字或元组。
"""
# 字典的访问
"""
    格式：字典的访问与元组、列表有所不同，元组和列表是通过数字索引
        获取对应的值，而字典是通过key值获取相应的value值。
        格式：value=dict[key]
    说明：字典的添加、删除和修改只需执行一条赋值语句即可，例如：
    dict[' x' ]=' value'
        字典没有remove操作。删除字典元素可调用内置函数del()完成。
    例子：字典的创建、添加、删除和修改
        dict = {'a':'apple', 'b':'banana', 'g':'grape', 'o':'orange'}
        print(dict)
        dict['w'] = 'watermelon'
        print(dict)
        del(dict['a'])
        print(dict)
        dict['g'] = 'grapefruit'
        print(dict)
    结果：
        {'a': 'apple', 'b': 'banana', 'g': 'grape', 'o': 'orange'}
        {'a': 'apple', 'b': 'banana', 'g': 'grape', 'o': 'orange', 'w': 'watermelon'}
        {'b': 'banana', 'g': 'grape', 'o': 'orange', 'w': 'watermelon'}
        {'b': 'banana', 'g': 'grapefruit', 'o': 'orange', 'w': 'watermelon'}
    字典函数
    方法                            作用
    clear()                         删除字典内所有元素
    copy()                          返回一个字典的浅复制
    fromkeys(seq)                   创建一个新字典，以序列seq中元素做字典
    get(key)                        返回指定键的值，如果键不在字典中，则返回default值
    items()                         以列表返回可遍历的(键，值)元组对
    keys()                          以列表返回字典所有的键
    values()                        以列表返回字典所有的值
    pop(keys)                       删除并返回字典指定key的值
    popitem()                       删除并返回字典的最后一个键值对，不接受参数
    setdefault(key,default=None)    和get相似，但如果键不存在字典中，将会添加键并将值设为default
    update(dict2)                   把字典dict2的键值对更新到dict里
    说明：
        popitem()返回并删除字典的某个键——值对，因此仅当不在乎字典元素的排列顺序时，此函数才适用。
        item()、keys()和values()都返回一个特殊对象——视图。视图被
        连接到原始字典，因此若字典发生变化，视图也相应地变化。
    例子：
        dict = {'a':'apple', 'b':'banana', 'c':'grape', 'd':'orange'}
        print(dict.keys())
        print(dict.values())
        print(dict.get('c'))
        print(dict.get('e'))
        dict1 = {'a':'apple', 'b':'banana'}
        print(dict1)
        dict2 = {'c':'grape', 'd':'orange'}
        print(dict2)
        dict1.update(dict2)
        print(dict1)
    结果：
        dict_keys(['a', 'b', 'c', 'd'])
        dict_values(['apple', 'banana', 'grape', 'orange'])
        grape
        None
        {'a': 'apple', 'b': 'banana'}
        {'c': 'grape', 'd': 'orange'}
        {'a': 'apple', 'b': 'banana', 'c': 'grape', 'd': 'orange'}
    例子：
        color = {'red': 1, 'blue': 2, 'green': 3, 'orange': 4}
        print(color)
        k = color.keys()
        for i in k:
            print(i)
        print(color.pop('red'))
        for i in k:
            print(i)
    结果：
        {'red': 1, 'blue': 2, 'green': 3, 'orange': 4}
        red
        blue
        green
        orange
        1
        blue
        green
        orange
    例子：字典的排序。字典的排序可以使用内置函数sorted()实现 # sorted(iterable,key=None,reverse=False)-->new sorted list
        dict = {'a': 'apple', 'b': 'banana', 'c': 'grape', 'd': 'orange'}
        print(dict)
        print(sorted(dict.items(), key=lambda d: d[0]))
        print(sorted(dict.items(), key=lambda d: d[1]))
    结果：
        {'a': 'apple', 'b': 'banana', 'c': 'grape', 'd': 'orange'}
        [('a', 'apple'), ('b', 'banana'), ('c', 'grape'), ('d', 'orange')]
        [('a', 'apple'), ('b', 'banana'), ('c', 'grape'), ('d', 'orange')]
    例子：字典的拷贝
        import copy
        dict = {'a': 'apple', 'b': {'g': 'grape', 'o':'orange'}}
        print(dict)
        dict1 = copy.deepcopy(dict)     # 对dict的深拷贝，即新建了dict2,修改不会对dict产生影响
        dict2 = copy.copy(dict)         # 对dict的浅拷贝，即对dict的引用，修改时会对dict产生影响
        dict1['b']['g'] = 'orange'
        print(dict)
        dict2['b']['g'] = 'orange'
        print(dict)
    结果：
        {'a': 'apple', 'b': {'g': 'grape', 'o': 'orange'}}
        {'a': 'apple', 'b': {'g': 'grape', 'o': 'orange'}}
        {'a': 'apple', 'b': {'g': 'orange', 'o': 'orange'}}
"""
# 集合
"""
    在Python中，集合是一系列不重复的元素。集合类似于字典，但只包含
    键，而没有相关联的值。
    在Python中，集合是相对较新的功能，在其还不支持集合时，一般使用字典模拟集合。
    集合分为两类：可变集合（set）和不可变集合（frozenset）。对于
    可变集合，可添加和删除元素，而不可变集合一旦创建就不能更改。
    与字典一样，集合的元素排列顺序也是不确定的。
    集合没有列表和字典用的多，本章简要介绍，详细内容可参阅：
    https://docs.python.org/3/library/stdtypes.htm#set
"""
# 集合基本功能
"""
    包括关系测试和消除重复元素。集合对象还支持union（联合）
    ，intersection(交)，difference（差）和sysmmetic difference(对称差集，
    即异或)等数学运算。
    大括号或set()函数可以用来创建集合。
    注意：想要创建空集合，必须使用set()而不是{}。
    例子：创建集合
        basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
        print(basket)
        print(type(basket))
        fruit = set(basket)
        print(fruit)
        print(type(fruit))
        print('orange' in fruit)
        print('crabgrass' in fruit)
    结果：
        ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
        <class 'list'>
        {'banana', 'apple', 'orange', 'pear'}       # 剔除重复元素
        <class 'set'>
        True
        False
    例子：集合运算
        a = set('abracadabra')
        b = set('alacazam')
        print(a)
        print(b)
        print(a - b)    # 差运算 （在a不在b的元素）
        print(a | b)    # 或运算 （ab并集） 
        print(a & b)    # 并运算 （ab交集）
        print(a ^ b)    # 异或运算（在a或在b，但不同时在ab的元素）
    结果：
        {'r', 'd', 'b', 'c', 'a'}
        {'z', 'm', 'c', 'l', 'a'}
        {'d', 'r', 'b'}
        {'r', 'z', 'd', 'm', 'b', 'c', 'l', 'a'}
        {'a', 'c'}
        {'r', 'z', 'd', 'm', 'l', 'b'}
"""
