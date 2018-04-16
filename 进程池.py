from multiprocessing import Process,Pool,freeze_support
import time,os

def Foo(i):
    time.sleep(2)
    print('from the %s'%os.getpid())
    return i+100

def Bar(arg):
    print('-->exec done:',arg)   #主进程调用

if __name__ == '__main__':

    pool = Pool(3) #允许同时放入3个进程
    print(os.getpid())
    for i in range(10):
        # pool.apply(func=Foo,args=(i,)) #串行
        pool.apply_async(func=Foo,args=(i,),callback=Bar)  #并行

    print('end')
    pool.close()  #需要先执行关闭再执行join，否则会报错AssertionError
    pool.join()  #等待进程结束，如果注释不执行apply_async中的callback，直接关闭
