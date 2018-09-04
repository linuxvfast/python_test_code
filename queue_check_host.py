import threading
import subprocess
from queue import Queue
from queue import Empty

whether = []

def is_alive(ip):
    '''
    检查主机是否存货
    :param ip: 需要检查的ip地址
    :return: 主机是否存货的结果
    '''
    if subprocess.call(["ping","-c","2",ip]):
        whether.append('{0} is alive'.format(ip))
    else:
        whether.append('{0} is down'.format(ip))

def call_whether(q):
    try:
        while True:
            ip = q.get_nowait()  #不阻塞
            is_alive(ip)
    except Empty:
        pass


def main():
    q = Queue()
    with open('ips.txt','r') as f:
        for line in f:
            q.put(line) #读取的ip放到队列中

        threads = []
        for line in range(10):
            thr = threading.Thread(target=call_whether,args=(q,))
            thr.start()
            threads.append(thr)

        #等待所有的线程执行完毕
        for thr in threads:
            thr.join()
            
        print('========================')
        for whe in whether:#打印检测结果
            print(whe)

if __name__ == '__main__':
    main()
