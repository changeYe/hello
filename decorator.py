import time


# def is_can_time():
#     start_time = time.time();
#     time.sleep(3)
#     end_time = time.time()
#     print("调用所需时间 %s",(end_time-start_time))
#
# is_can_time()

#
# def timer(func):
#     def two():
#         start_time = time.time();
#         func()
#         end_time = time.time()
#         print("调用所需时间 %s",(end_time-start_time))
#     return two
#
# @timer
# def is_can_time():
#     time.sleep(3)
#
# is_can_time()

# 函数携带参数
# def timer(func):
#     def two(a,b):
#         print('start')
#         func(a,b)
#         print('stop')
#     return two
#
# @timer
# def is_can_time(a,b):
#     print(a+b)
# is_can_time(2,3)

# 装饰器注解中传递参数


def timer(arge):
    def one(func):
        def two(a, b):
            print('start ' + arge + '====' + func.__name__)
            func(a, b)
            print('stop ' + arge)

        return two

    return one


@timer('add')
def is_can_time(a, b):
    print(a + b)


@timer('dele')
def dele(a, b):
    print(a + b)


is_can_time(2, 3)
dele(2, 30)
