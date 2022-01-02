# 面向对象基础
# 类与对象
"""
    现实生活中的每一个相对独立的事物丢可以看做一个对象。
    每个对象都具有描述其特征的属性及附属它的行为。
    面向对象程序设计是一种计算机编程架构。它有以下三种基本特性：
        封装性(Encapsulation)
        继承性(Inheritance)
        多态性(Polymorphism)

"""
# 对象的概念
"""
    将数据以及数据的操作封装在一起，组成一个相互依存、不可分割的整体，即对象。
    对于详图类型的对象进行分类、抽象后，得出共同的特征而形成了类。
    数据抽象——型号，品牌，换挡数。
    代码抽象——Break()，SpeedUp()，ChangShift()，Run()，Stop()
"""
# 类的定义
"""
    格式：class Class_name：
            ...
    例子：
        class Person(object):
            def __init__(self):  # 类的构造函数，用来初始化对象
                self.name = ''
                self.age = 0
            def display(self):  # 类中定义的函数也称为方法
                print('person(%s, $d)' % (self.name, self.age))
"""
# 对象的创建
"""
    创建对象的过程称为实例化
    特征：对象的标识、属性和方法。
    对象的标识用于区分不同的对象，当对象被创建之后，该对象会获取一块存储
    空间，存储空间的地址即为对象的标识。对象的属性和方法与类的成员变量和
    成员函数相对应。
    例子：
        class Person(object):
            def __init__(self):  # 类的构造函数，用来初始化对象
                self.name = ''
                self.age = 0
        
            def display(self):  # 类中定义的函数也称为方法
                print('Person(%s, %d)' % (self.name, self.age))
        
        
        if __name__ == '__main__':  # 判断当前模块是不是直接被执行的
            p = Person()  # 为Person类定义的一个对象，叫p
            print(p)
            print(p.age)
            print(p.name)
            p.age = 25  # 对象赋值
            p.name = 'jack'
            p.display()  # 调用display()这个方法
    结果：
        <__main__.Person object at 0x0000022C97978880>   #存储空间
        0   # 初始化的年龄
            # 初始化的名字
        Person(jack, 25)    # 赋值后的名字，年龄
"""
# 属性与方法
"""
    类是由属性和方法组成。类的属性是对数据的封装，而类的方法则表示对象具有的行为。
    类通常由函数（实例方法）和变量（类变量）组成。
    Python的构造函数、析构函数、私有属性或方法都是通过名称约定区分的。
    类的属性
        Python的类的属性一般分为私有属性和公有属性，像C++有定义属性的关键字
        (public、private、protect)，Python没有这类关键字，默认情况下所有的属
        性都是“公有的”，对公有属性的访问没有任何限制，且都会被子类继承，也
        能从子类中进行访问。
        若不希望类的属性在类外被直接访问，就要定义为私有属性。
        Python使用约定属性名称来划分属性类型。若属性的名字以两个下划线开始，表
        示私有属性；反之，没有使用双下划线开始的表示公有属性。类的方法也同样使用
        这样的约定。
        Python没有保护类型的修饰符。
        Python的实例属性和静态属性。
            实例属性：是以self为前缀的属性，没有该前缀的属性是普通的局部变量。
                      C++中有一类特殊的属性称为静态变量。静态变量可以被类直接
                      调用，而不被实例化对象调用。
                      在Python中静态变量称为类变量，类变量可以在该类的所有实
                      例中被共享。
            例子：
                class Fruit(object):
                    price = 0  # 类属性
                
                    def __init__(self):
                        self.color = 'red'  # 实例属性
                        zone = "China"  # 局部属性
                
                
                if __name__ == '__main__':
                    print(Fruit.price)  # 使用类名调用类变量
                    apple = Fruit()  # 实例化apple
                    print(apple.color)  # 打印apple实例化的颜色
                    Fruit.price = Fruit.price + 10  # 将类变量加10
                    print('apple price=' + str(apple.price))  # 打印apple实例的price
                    banana = Fruit()
                    banana.color = 'yellow'
                    print(banana.color)
                    print('banana price = ' + str(banana.price))
            结果：
                0
                red
                apple price=10
                yellow
                banana price = 10
        
            关于Python私有属性的访问：
                类的外部不能直接访问私有属性。
                但Python为了方便测速，便提供了方法：
                私有属性访问的格式：
                instance._classname__attribute
                注意：classname之前是单下划线
                      attribute之前是双下划线
                说明：instance表示实例化对象名；
                      classname表示类名；
                      attribute表示私有属性。
                例子：访问私有属性
                    class Fruit(object):
                        def __init__(self):
                            self.__color = 'red'  # 定义私有变量(两个下划线表示这是私有属性)
                    if __name__ == '__main__':
                        apple = Fruit()  # 实例化apple
                        print(apple._Fruit__color)  # 调用类的私有变量
                结果：
                    red
            注意：Python对类的属性和方法的定义次序并没有要求。合理的方式是将类属性定义在类
                  中最前面，然后再定义私有方法，最后定义公有方法。
                  Python的类还提供了一些内置属性，用于管理类的内部关系。
                  例如：__dict__,__bases__,__doc__等。
    类的方法：
        类的方法也分为公有方法和私有方法。私有方法不能被模块外的类或方法调用，
        私有方法也不能被外部的类或函数调用。
        C++ 中的静态方法使用关键词static声明，而Python使用函数staticmethod()
        或@staticmethod修饰器将普通的函数转换为静态方法
        例子：
            class Fruit(object):
                price = 0
            
                def __init__(self):
                    self.__color = 'red'  # 定义私有变量
            
                def getColor(self):
                    print(self.__color)
            
                @staticmethod  # 定义静态变量
                def getPrice():
                    print(Fruit.price)
            
                def __getPrice():  # 定义私有函数
                    Fruit.price = Fruit.price + 10
                    print(Fruit.price)
            
                count = staticmethod(__getPrice)
            
            
            if __name__ == '__main__':
                apple = Fruit()
                apple.getPrice()  # 使用实例调用静态方法
                Fruit.count()  # 使用类名调用静态方法
                banana = Fruit()
                Fruit.getPrice()
                Fruit.count()   
        结果：
            0
            10
            10
            20
        __init__方法：构造函数用于初始化类的内部状态，为类的属性设置默认值。
                      C++的构造函数是与类同名的方法，而Python的构造函数名为__init__。
                      __init__方法是可选的，若不提供__init__方法，Python将会给出1个
                      默认的__init__方法。
        类的内置方法：
        内置方法                    描述
        __init__(self,...)          初始化对象，在创建对象时调用
        __del__(self)               释放对象，在对象被删除时调用
        __str__(self)               生成对象的字符串表示，在使用print语句时被调用
        __repr__(self)              生成对象的官方表示，在使用print语句时被调用
        __getitem__(self,key)       获取序列的所有key对应的值，等价于seq[key]
        __len__(self)               在调用内联函数len()时被调用
        __cmp__(src,dst)            比较两个对象src和dst
        __getattr__(self,name)      获取属性的值
        __getattribute__(self,name) 获取属性的值，能更好的控制
        __setattr__(self,name,val)  设置属性的值
        __delattr__(self,name)      删除name属性
        __call__(self,*args)        将实例对象作为函数使用
        __gt__(self,other)          判断self对象是否大于other
        __lt__(self,other)          判断self对象是否小于other
        __ge__(self,other)          判断self对象是否大于或等于other
        __le__(self,other)          判断self对象是否小于或等于other
        __eg__(self,other)          判断self对象是否等于other
"""


class Fruit(object):
    price = 0

    def __init__(self):
        self.__color = 'red'  # 定义私有变量

    def getColor(self):
        print(self.__color)

    @staticmethod  # 定义静态变量
    def getPrice():
        print(Fruit.price)

    def __getPrice():  # 定义私有函数
        Fruit.price = Fruit.price + 10
        print(Fruit.price)

    count = staticmethod(__getPrice)


if __name__ == '__main__':
    apple = Fruit()
    apple.getPrice()  # 使用实例调用静态方法
    Fruit.count()  # 使用类名调用静态方法
    banana = Fruit()
    Fruit.getPrice()
    Fruit.count()
