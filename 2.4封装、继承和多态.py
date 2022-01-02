# 封装、继承、多态
# 封装
"""
    封装就是把抽象的数据和对数据进行的操作封装在一起，数据被保存在内部，
    程序的其他部分只有通过被授权的操作（成员方法）才能对数据进行操作。
"""
# 继承
"""
    继承是面向对象的重要特征之一，可实现代码的重用。
    通过继承可以创建新类，给既有类的副本添加变量和方法。
    原始的类称为父类或超类，新类称为子类或派生类。
    关于在单继承关系中的构造函数：Python中如果子类有自己的构造函数，不会自动调用父类的构造函数
        如果需要用到父类的构造函数，则需要在子类的构造函数中显式地调用。
        如果子类需要扩展父类的行为，可以添加__init__方法的参数。
    使用继承
        当类设计完成之后，就可以考虑类之间的逻辑关系，可以采用UML工具表示类之间的关系。
    例子：
        class Fruit(object):  # 基类
        def __init__(self, color):
            self.color = color
            print('Fruit color: %s' % self.color)
        def grow(self):
            print('grow...')
            
        class Apple(Fruit):
            def __init__(self, color):
                Fruit.__init__(self, color)  # Fruit color: red
                print('apple color: %s' % self.color)  # apple color: red
    
        class Banana(Fruit):
            def __init__(self, color):
                Fruit.__init__(self, color)
                print('Banana color: %s' % self.color)
            def grow(self):
                print('Banana grow...')
        
        if __name__ == '__main__':
            apple = Apple('red')
            apple.grow()
            banana = Banana('yellow')
            banana.grow()
    结果：
        Fruit color: red
        apple color: red
        grow...
        Fruit color: yellow
        Banana color: yellow
        Banana grow...
        
    例子：在上一讲的一般人基础上增加MIT人员的内容
        class Person(object):
            def __init__(self, name):
                self.name = ""
                self.age = 0
        
        class MITPerson(Person):
            nextIdNum = 0
        
            def __init__(self, name):
                Person.__init__(self, name)
                self.idNum = MITPerson.nextIdNum
                MITPerson.nextIdNum += 1
        
            def getIdNum(self):
                return self.idNum
        
            def __lt__(self, other):  # lt内建方法的重新定义，是long的l，不是I
                return self.idNum < other.idNum
        
        if __name__ == "__main__":
            p1 = MITPerson("Eric")
            p2 = MITPerson("John")
            p3 = MITPerson("John")
            p4 = Person("John")
        
            print(p1)
            print(p1.getIdNum())
            print(p2.getIdNum())
            print(p3.getIdNum())
            print(p4)
            print(p1 < p2)
            print(p3 < p2)
            print(p1 < p4)
    结果：
        <__main__.MITPerson object at 0x0000025866E88550>
        0
        1
        2
        <__main__.Person object at 0x0000025866F27490>
        True
        False
        Traceback (most recent call last):
          File "D:/AA啥都有/Study/2019-2020第一学期/Python/2.4封装、继承和多态.py", line 90, in <module>
            print(p1 < p4)
          File "D:/AA啥都有/Study/2019-2020第一学期/Python/2.4封装、继承和多态.py", line 74, in __lt__
            return self.idNum < other.idNum
        AttributeError: 'Person' object has no attribute 'idNum'
        
        报错的原因是因为p1是MITPerson类，而p4是Person类，前者有IdNum而后者没有，即'Person' object has no attribute 'idNum'
    
    例子：在上述类的基础上定义Student类及其子类：
        上述代码+
        class Student(MITPerson):
            pass
        
        
        class UG(Student):
            def __init__(self, name, classYear):
                MITPerson.__init__(self, name)
                self.year = classYear
        
            def getClass(self):
                return self.year
        
        
        class Grad(Student):
            pass
        
        
        if __name__ == "__main__":
            s1 = UG('Fred', 2016)
            s2 = Grad('Angela')
            print(isinstance(s1, Student))  # 判断s1和Student之间是不是派生关系
            print(isinstance(s2, Student))
    结果：
        True
        True
        
    抽象基类：
        使用继承之后，子类可以重用父类中的属性和方法，且可对继承的方法进行重写
        抽象基类是对一类事物的特征行为的抽象，由抽象方法组成。
        在Python3中可以使用abc模块，该模块中有一个元类ABCmeta和修饰器@abstractmethod。
        不能被直接实例化
    例子：抽象基类的应用
        from abc import ABCMeta, abstractmethod
    
        class Fruit(metaclass=ABCMeta):         #声明该类为抽象类
            @abstractmethod                     #声明该函数为抽象函数
            def grow(self):
                pass
        
        class Apple(Fruit):
            def grow(self):
                print('Apple growing')
        
        if __name__ == '__main__':
            apple = Apple()
            apple.grow()
    结果：
        Apple growing
        
    多重继承：
        Python支持多重继承，即一个类可以继承多个父类。
        多重继承的语法格式：class_name(parent_class1,parent_class2...),
        其中class_name是类名，parent_class1和parent_class2是父类名。
    多重继承关系中的构造函数：
        子类从多个父类派生，而子类又没有自己的构造函数时：
        如果最前面第一个父类没有构造函数，则继承第2个的构造函数，第2个没有的话，再往后找，以此类推。
    例子：多重继承应用
        class Fruit(object):
            def __init__(self):
                print('initialize Fruit')
        
            def grow(self): # 定义grow方法
                print('growing...')
        
        
        class Vegetable(object):
            def __init__(self):
                print('initialize Vegetable')
        
            def plant(self):    # 定义plant方法
                print('planting...')
        
        
        class Watermelon(Vegetable, Fruit):
            pass
        
        
        if __name__ == '__main__':
            w = Watermelon()
            w.grow()
            w.plant()    
    结果：
        initialize Vegetable
        growing...
        planting...        
"""
# 多态
"""
    继承机制说明子类机具有父类的公有属性和方法，而且子类可以扩展自身的功能，添加新的
属性和方法。因此，子类可以替代父类对象，这种特性称为多态性。
    此外，从根本上说，所谓多态性是指当不同的对象收到相同的消息时，产生不同的动作。
    
    例子：Apple、Banana类继承了Fruit类，因此Apple、Banana具有Fruit类的共性。Apple、Banana类的
          实例可以替代Fruit对象，同时又呈现出各自的特性。
        class Fruit(object):
            def __init__(self, color=None):
                self.color = color
        
        
        class Apple(Fruit):
            def __init__(self, color='red'):
                Fruit.__init__(self, color)
        
        
        class Banana(Fruit):
            def __init__(self, color='yellow'):
                Fruit.__init__(self, color)
        
        
        class FruitShop(object):
            def sellFruit(self, fruit):
                if isinstance(fruit, Apple):
                    print('sell Apple')
                if isinstance(fruit, Banana):
                    print('sell Banana')
                if isinstance(fruit, Fruit):
                    print('sell Fruit')
        
        
        if __name__ == "__main__":
            shop = FruitShop()
            apple = Apple()
            banana = Banana()
            shop.sellFruit(apple)   # apple是Apple和Fruit类的对象，所以前两句话在这里产生。
            shop.sellFruit(banana)  # banana是Banana和Fruit类的对象，所以后两句话在这里产生。
    结果：
        sell Apple
        sell Fruit
        sell Banana
        sell Fruit
"""



