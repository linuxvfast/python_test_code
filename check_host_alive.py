import threading
import subprocess

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


def main():
    with open('ips.txt','r') as f:
        lines = f.readlines()
        threads = []
        for line in lines:
            thr = threading.Thread(target=is_alive,args=(line,))
            thr.start()
            threads.append(thr)
        
        #等待所有的线程执行完毕
        for thr in threads:
            thr.join()

        for whe in whether:#打印检测结果
            print(whe)




if __name__ == '__main__':
    main()
