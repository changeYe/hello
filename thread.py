import threading
import time

def thread_method(a,b):
    print("开始打印")
    time.sleep(2)
    print("这里是就是一个%s 普通打印%s " %(a,b))

# 这里是普通打印
# for i in range(1,6,1):
#     thread_method(i,i+1)

# 线程打印
# for i in range(1,6,1):
#     t1 = threading.Thread(target=thread_method, args=(i,i+i))
#     t1.start()

# print(threading.currentThread().name,'end')






