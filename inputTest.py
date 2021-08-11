# a = "abcdedj"
# year = input("请输入输入")
# print(a[int(year)%12])

a = "鼠牛虎兔龙蛇马羊猴鸡狗猪"

# for year in range(2000,2019):
#     # print(' %s 年 生肖 %s a'  %{year,int(year)%12})
#     print(' 年 %s 生肖 %s'  %(year, a[int(year)%12]))
#     # print(' %s 年 生肖 %s a'  %{year,a[year%12]})

# num = 5
# while True:
#     if num > 10:
#         break
#     num = num + 1
#     if num==7:
#         continue
#     else:
#      print(num)

#
# month = int(input("输入月"))
# day = int(input("输入天"))
# for to in range(len(a)) :
#     if a[to] >= (month,day):
#         print(a[to])
#         break
#     elif month == 12 and day > 25:
#         print(a[0])
#         break

# num = 10;
# if num >5 or num < 9:
#     print("hhh")
# else:
#     print("bb")

# dict = {}
# print(type(dict))
# dict['a'] = 1
# dict['b'] = {'b1':11,'b2':22}
# print(dict)

# data = {}
# num = 5
# for i in range(num):
#     data[i] = 0 # 先初始化
#     data[i] += 1 # 这里是根据下标查找 data['A'] += 1 这个是根据具体的值查找
#
# print(data)

# alist = []
# for i in range(1,11):
#     if i % 2 == 0:
#         alist.append(i*i)
#
# print(alist)
#
# blist = [ i*i for i in range(1,11) if (i%2==0)]
# print(blist)

cjson = {}
for i in range(1,11):
    cjson[i] = 0
print(cjson)

dJson = { i:0 for i in range(1,11)}
print(dJson)