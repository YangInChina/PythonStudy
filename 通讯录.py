"""
    创建字典类型的通讯录，分别完成以下操作：
    1）先建立只有三位舍友的字典变量，以手机号为键，值为姓名
    2）然后添加qq号到通讯录的字典变量中
    3）最后输入一个手机号进行查找，如果该同学在通讯录中，则输出他的所有信息，否则将其信息（手机号，姓名，QQ号）
        添加到通讯录的字典中。
"""


class RoomMate(object):
    def __init__(self):
        self.name = ''
        self.PhoneNumber = -1  # 为空时的值
        self.QQNumber = -1

    def display(self):
        print('RoomMate(%s, 手机号:%d , QQ号:%d)' % (self.name, self.PhoneNumber, self.QQNumber))

    def input(self):
        self.name = input("请输入姓名：")
        self.PhoneNumber = a
        self.QQNumber = int(input('请输入QQ号码：'))


if __name__ == '__main__':
    Mate1 = RoomMate()
    Mate1.name = '张三'
    Mate1.QQNumber = 1601860918
    Mate1.PhoneNumber = 18309254582

    Mate2 = RoomMate()
    Mate2.name = '李四'
    Mate2.PhoneNumber = 17191908953
    Mate2.QQNumber = 1970896113

    Mate3 = RoomMate()
    Mate3.name = '王麻子'
    Mate3.PhoneNumber = 15002968441
    Mate3.QQNumber = 2045577912

    Mate4 = RoomMate()
AddressList = {18309254582: Mate1, 1970896113: Mate2, 2045577912: Mate3}
switch = 1
while switch == 1:
    a = int(input('请输入查询的手机号：'))
    if AddressList.get(a) is None:
        k = int(input('未找到结果，是否保存为新的联系人（1，是/2，否）：'))
        if k == 1:
            Mate4.input()
            Mate4.display()
            AddressList[a] = Mate4
            AddressList.get(a)
        else:
            switch = 0
            break
    else:
        AddressList.get(a).display()

    k = int(input('是否继续查找？（1，是/2，否）：'))
    if k == 1:
        switch = 1
    else:
        switch = 0
        break
