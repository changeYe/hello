# file1 = open('name.txt','w')
# file1.write("诸葛亮")
# file1.close()
#
# file2 = open('name.txt','a')
# file2.write("刘备")
# file2.close()
#
try:
    raise ValueError('不对')
except ValueError as v:
    print(v)

# try:
#     a = open('name.txt')
# except Exception as e:
#     print(e)
# finally:
#     a.close()
