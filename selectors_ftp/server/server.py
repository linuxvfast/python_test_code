import selectors
import socket
import os
import queue
import json
import base64

"""
401：文件不存在
402：文件已存在
403：命令错误
200：正常状态返回值
"""


class LinuxConnectLost(Exception):

    def __init__(self, msg):
        self.message = msg


class Ftp(object):

    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.queue_dict = {}
        self.fd_dict = {}
        self.host_dict = {}

    def accept(self, sock, mask):
            conn, addr = sock.accept()
            conn.setblocking(False)
            print('【%s:%d】连接到服务器...' % (addr[0], addr[1]))
            self.host_dict[conn] = addr
            self.queue_dict[conn] = queue.Queue(0)
            self.sel.register(conn, selectors.EVENT_READ, self.read)

    def read(self, conn, mask):

        try:
            data = conn.recv(4096)
            if data:
                self.queue_dict[conn].put(data)  # 将接收到的数据放入序列中
            else:
                raise LinuxConnectLost('[LinuxError 10000] Linux客户端断开')
        except (ConnectionResetError, LinuxConnectLost, ConnectionAbortedError) as e:
            self.sel.unregister(conn)
            conn.close()
            del self.queue_dict[conn]
            print('【%s:%d】连接关闭...' % (self.host_dict[conn][0], self.host_dict[conn][1]))

    def cmd_put(self, conn, data):
        print('【%s:%d】开始上传文件...' % (self.host_dict[conn][0], self.host_dict[conn][1]))
        if os.path.isfile(data['filename']):
            print(data['filename'])
            conn.send(b'402')
            return
        f = open(data['filename'], 'wb')
        file_info = {
            'fd': f,
            'size': data['size'],
            'write_size': 0
        }
        self.fd_dict[conn] = file_info
        conn.send(b'200')

    def cmd_get(self, conn, data):
        print('【%s:%d】开始下载文件...' % (self.host_dict[conn][0], self.host_dict[conn][1]))
        if not os.path.isfile(data['filename']):
            data1 = {
                'action': 'ERROR',
                'code': '401'
            }
            conn.sendall(json.dumps(data1).encode('utf-8'))
            return
        f = open(data['filename'], 'rb')
        size = os.path.getsize(data['filename'])
        file_info = {
            'fd': f,
            'size': size,
            'read_size': 0
        }
        self.fd_dict[conn] = file_info
        data2 = {
            'action': 'OK',
            'size': size
        }
        conn.send(json.dumps(data2).encode('utf-8'))

    def cmd_write(self, conn, data):
        """
        data内容：{
            action:write,
            file_data: 客户端发送来的文件内容
            }
        :param conn:
        :param data:
        :return:
        """
        file_info = self.fd_dict[conn]
        f = file_info['fd']
        size = file_info['size']
        write_size = file_info['write_size']
        file_data = base64.b64decode(data['file_data'].encode())
        f.write(file_data)
        write_size += len(file_data)
        if write_size < size:
            self.fd_dict[conn]['write_size'] = write_size
        else:
            del self.fd_dict[conn]
            f.close()
            print('【%s:%d】上传文件完成...' % (self.host_dict[conn][0], self.host_dict[conn][1]))
        conn.send(b'200')

    def cmd_read(self, conn, data):
        """
        data内容：{
            action: read
        }
        :param conn:
        :param data:
        :return:
        """
        file_info = self.fd_dict[conn]
        f = file_info['fd']
        size = file_info['size']
        read_size = file_info['read_size']
        file_data = f.read(1024)
        conn.sendall(file_data)
        read_size += len(file_data)
        if read_size < size:
            self.fd_dict[conn]['read_size'] = read_size
        else:
            f.close()
            print('【%s:%d】读取文件完成...' % (self.host_dict[conn][0], self.host_dict[conn][1]))
            del self.fd_dict[conn]

    def run(self):
        sock = socket.socket()
        sock.bind(('0.0.0.0', 9999))
        sock.listen(100)
        sock.setblocking(False)
        self.sel.register(sock, selectors.EVENT_READ, self.accept)
        while True:
            events = self.sel.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)
            for key1 in self.queue_dict.keys():
                try:
                    data = self.queue_dict[key1].get_nowait()
                except queue.Empty as e:
                    continue
                data_dict = json.loads(data.decode())
                if hasattr(self, 'cmd_%s' % data_dict['action']):
                    func = getattr(self, 'cmd_%s' % data_dict['action'])
                    func(key1, data_dict)
                else:
                    key1.send(b'403')    # 命令错误


ftp = Ftp()
ftp.run()



