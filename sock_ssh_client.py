__author__ = 'progress'

import socket

client = socket.socket()
client.connect(('localhost',9999))
while True:
    cmd = input('>>:').strip()
    client.send(cmd.encode())
    cmd_res_size = client.recv(1024)
    print('接收的数据大小:',cmd_res_size)
    client.send('我准备好了,可以发送数据了...'.encode('utf-8'))
    rece_data = b''
    recv_size = 0
    while recv_size != int(cmd_res_size.decode()):
        data = client.recv(1024)
        print('每次接收的长度:',len(data))
        recv_size += len(data)
        rece_data += data
    print('接收完成返回的数据:',rece_data.decode('utf-8'))

client.close()