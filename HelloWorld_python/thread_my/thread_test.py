#encoding=utf8
import time
import threading


# 多线程有两种方式：
# 1.调用thread模块中的start_new_thread()
# 2.继承 threading.Thread ，重写 __inti__ 和 run 方法

def thread_new():
    try:
        threading.start_new_thread(print_test, ('TA',))
        threading.start_new_thread(print_test, ('TB',))
    except:
        print (1)
    pass

def thread_extend():
    pass

def print_test(tName):
    print (tName)
    print (threading.currentThread().ident)
    for i in range(100):
        print(tName+str(i))


def main():
    print(threading.currentThread().ident)
    thread_new()
    time.sleep(3)
    print ('over')
    pass

if __name__ == '__main__':
    main()