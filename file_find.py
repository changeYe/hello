import re
# def find(hero):
#     with open('sanguo_utf8.txt',encoding='utf-8') as f:
#         data = f.read().replace('\n','')
#         name_num = re.findall(hero,data)
#         print(" 主角 %s 出现 %s 次" %(hero,len(name_num)))
#     return len(name_num)
#
# with open('name.txt',encoding='utf-8') as f:
#     for line in f:
#         names = line.split("|")
#         for name in names:
#             find(name)

# for i in range(1,10,2):
#     print(i)

# num = 1;
# def frange(start,stop,step):
#     num = start
#     while num <= stop:
#         yield num
#         num += step
#
# for i in frange(1,10,0.5):
#     print(i)
#
# lambda :True
# def func(name):
#     print(name)
# func(111)
# print(lambda name:print(name+"4444"))

# import redis
# ip = '172.24.36.103'
# password = ''
# conn_pool = redis.ConnectionPool(host=ip,password=password, port=6379)
# r = redis.Redis(connection_pool=conn_pool)
# r.set(name="tongqin", value="8-10")
# print(r.keys("*"))


# pip install redis
#
# for i in zip((1,2,3),(4,5,6)):
#  print(i)

from functools import reduce

num =reduce(lambda x,y:x+y,{1,2,3},1)
print(num)
