# class Player():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(' 姓名 %s 年龄 %s ' %(self.name,self.age))
#
# user1 = Player('张三',18)
# user2 = Player('李四',28)
# user1.print_info()
# user2.print_info()


# class Player():
#     def __init__(self,name,age,phone):
#         self.__name = name
#         self.age = age
#         self.phone = phone
#     def print_info(self):
#         print(' 姓名 %s 年龄 %s 电话号码 %s' % (self.__name, self.age,self.phone))
#
#     def setName(self,name):
#         self.__name = name
#
# class Monster():
#     pass

# user1 = Player('张三',18,'123')
# user2 = Player('李四',28,'456')
# user1.print_info()
# user1.setName('王五')
# # user1.__name = '王五'
# user1.print_info()
# user2.print_info()

# from abc import ABC
#
#
# # 继承
# class Animals(ABC):
#     def __init__(self, age):
#         self.age = age
#
#     def run(self):
#         return '' + str(self.age) + '在跑了'
#
#
# class Boss(Animals):
#     def __init__(self, age):
#         self.age = age
#         super().__init__(age)
#
#     def run(self):
#         return 'Boss:' + str(self.age) + '在跑路'
#
# dict
# from urllib.request import urlopen
# class Dogface(Animals):
#
#     def run(self):
#         return 'dogface 小兵: {} 在跑路' .format(1)
#
# boss = Boss(1)
# boss1 = Boss(age=1)
# print(boss.run())
# user1 = Animals(90)
# user2 = Boss(90)
# user3 = dogface(900)
#
# print(user1.run())
# print(user2.run())
# print(user3.run())
#
# print(type(user1))
# print(type(user2))
# print(type(user3))
#
# print(isinstance(user1, object))
# print(isinstance(user2, Animals))
# print(isinstance(user1, Animals))
# print(isinstance('abd', object))
# print(isinstance(123, object))


class TestWith():
    def __enter__(self):
        print("进入方法")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('结束退出')
        if exc_tb is None:
            print("正查干退出")
        else:
            print('有异常情况 %s' %exc_tb)

with TestWith():
    print('干就完')
    raise NameError('有异常情况，抛出')