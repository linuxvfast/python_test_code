__author__ = 'progress'

import os,socket

server = socket.socket()
server.bind(('localhost',9999))
server.listen()
print('等待客户端连接...')
while True:
    conn,addr = server.accept()
    print('接收到数据:',addr)
    while True:
        date = conn.recv(1024)
        print('执行的命令:',date)
        # if not date:
        #     print('输入为空')
        #     break
        cmd_res = os.popen(date.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = 'cmd exec success,has not notput...'
        conn.send(str(len(cmd_res.encode())).encode())  #告诉长度
        client_ack = conn.recv(1024)    #处理粘包
        print('客户端开始接收数据了...')
        conn.send(cmd_res.encode('utf-8'))

server.close()