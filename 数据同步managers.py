from multiprocessing import Process,Manager
import os
def f(d,l):
    # d[1] = '1'
    # d['2'] = 2
    # d[0.25] = None
    # l.append(1)
    d[os.getpid()] = os.getppid()
    l.append(os.getpid())
    print(l)


if __name__ == '__main__':
    with Manager() as Manager:
        d = Manager.dict()

        l = Manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=f,args=(d,l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)