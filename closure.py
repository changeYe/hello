# 闭包
# def func():
#     a = 1;
#     b = 2;
#     return a+b;
# print(func())
# def num(a):
#     def add_one(b):
#         return a+b
#     return add_one
# add = num(1)
# print(add(2))


def one(start=0):
    a = [start]
    def two():
        a[0] +=  1
        return a[0]
    return two
num1 = one(1);
num2 = one(10);
print(num1())
print(num2())
print(num2())

