__author__ = 'progress'

import socket
import os,hashlib

server = socket.socket()
server.bind(('localhost',9999))
server.listen()
while True:
    print('等待客户端的链接...')
    conn,addr = server.accept()
    print('已经链接:',addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('client has exit...')
            break
        print('recv the data from client:',data.decode())
        # f = open('sock_ssh_client.py','r',encoding='utf-8')
        # conn.send(f.read().encode())
        cmd,filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f = open(filename,'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())
            conn.recv(1024)
            for line in f:
                m.update(line)
                conn.send(line)
            file_md5 = m.hexdigest()
            print('file md5:',file_md5)
            conn.send(file_md5.encode())
            f.close()


server.close()