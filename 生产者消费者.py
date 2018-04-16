import threading,time
import queue
q = queue.Queue(10)
def producer(name):
    count =0
    while True:
        q.put('骨头%s'%count)
        print('[%s] 生产骨头[%s]'%(name,count))
        count += 1
        time.sleep(1)

def consumer(name):
    while True:
        print('%s 取到 %s'%(name,q.get()))
        # time.sleep(2)

if __name__ == '__main__':
    s = threading.Thread(target=producer,args=('vfast',))
    s.start()

    x = threading.Thread(target=consumer,args=('test',))
    x.start()

    x1 = threading.Thread(target=consumer,args=('test1',))
    x1.start()