__author__ = 'progress'

import socket,hashlib

client = socket.socket()
client.connect(('localhost',9999))
while True:
    res = input('>>:').strip()
    if len(res) == 0:continue
    if res.startswith('get'):
        client.send(res.encode())
        data_size = client.recv(1024)
        print('recv data size:',data_size)
        client.send('已经可以接收文件...'.encode())
        file_total_size = int(data_size.decode())
        recv_size = 0
        filename = res.split()[1]
        f = open(filename+'.new','wb')
        m = hashlib.md5()
        while recv_size != file_total_size:
            if file_total_size - recv_size > 1024:
                size = 1024
            else:
                size = file_total_size - recv_size
            data = client.recv(size)
            recv_size += len(data)
            m.update(data)
            f.write(data)
        # print('recv data from server:',recv_data.decode())
        else:
            file_md5 = client.recv(1024)  #接收的md5
            print(file_md5)
            file2_md5 = m.hexdigest()  #客户端的文件md5值
            print(file2_md5)
            print('file recv success...')
            f.close()
client.close()
