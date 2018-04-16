from multiprocessing import Process,Queue

def f(q):
    q.put('\033[44;1m 42,hello,tom\033')

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())