import multiprocessing
import time
import threading

def tes(): #线程调用方法
    print('thread %s'%threading.get_ident())

def run(name): #进程调用方法
    time.sleep(2)
    print('process %s'%name)
    t = threading.Thread(target=tes)  #在进程中生成线程
    t.start()

if __name__ == '__main__':
    start_time = time.time()
    process_list = []
    for i in range(10): #生成10个进程
        p = multiprocessing.Process(target=run,args=('test',))
        p.start()
        process_list.append(p)

    for i in process_list:
        i.join()
    print('end time',time.time() - start_time)