from multiprocessing import Process,Pipe

def f(conn):
    conn.send([42,'hello',False])
    conn.close()


if __name__ == '__main__':
    parent_conn,child_conn = Pipe()
    p = Process(target=f,args=(parent_conn,))
    p.start()
    p.join()
    print('from child_conn recv:',child_conn.recv())
