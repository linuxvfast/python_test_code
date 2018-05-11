import selectors
import socket
import os
import json,time
import queue
import base64

BASE_DIR=os.path.dirname(os.path.abspath(__file__))  #获取FTP目录

class Selectros_ftp(object):
    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.download_dict = {}
        self.upload_dict = {}
        self.queue_dict ={}
        self.host_dict = {}


    def cmd_put(self,conn,data):
        file_path = '%s/%s'%(BASE_DIR,data['file_name'])
        f = open(data['file_name'], 'wb')
        file_info = {
            'fd': f,
            'size': data['size'],
            'write_size': 0
        }
        self.upload_dict[conn] = file_info
        conn.send(b'you can send file...')

    def cmd_write(self,conn,data):
        print('data',data)
        file_info = self.upload_dict[conn]
        f = file_info['fd']
        size = file_info['size']
        write_size = file_info['write_size']
        file_data = base64.b64decode(data['file_data'].encode())

        f.write(file_data)
        write_size += len(file_data)
        if write_size < size:
            self.upload_dict[conn]['write_size'] = write_size
        else:
            del self.upload_dict[conn]
            f.close()
            print('文件接收成功')
        conn.send(b'200')

    def cmd_get(self,conn,data):
        '''
        :param conn: 当前的连接
        :param data={'action': 'get', 'file_name': 'test.exe'}:
        :return:
        '''
        file_path = '%s/%s'%(BASE_DIR,data['file_name'])
        if not os.path.isfile(file_path):
            data1 = {
                'action': 'Error',
                'code': '401'
            }
            conn.sendall(json.dumps(data1).encode())
            return
        f = open(file_path, 'rb')
        size = os.path.getsize(file_path)
        file_info = {
            'fd': f,
            'size': size,
            'read_size': 0
        }
        self.download_dict[conn] = file_info
        data2 = {
            'action': 'OK',
            'size': size
        }
        conn.send(json.dumps(data2).encode())

    def cmd_read(self,conn,data):
        '''读取文件内容'''
        file_info = self.download_dict[conn]
        f = file_info['fd']
        size = file_info['size']
        read_size = file_info['read_size']
        file_data = f.read(1024)
        conn.sendall(file_data)
        read_size += len(file_data)
        if read_size < size:
            self.download_dict[conn]['read_size'] = read_size
        else:
            f.close()
            del self.download_dict[conn]
            print('文件发送完成')

    def accept(self,sock, mask):
        conn, addr = sock.accept()  # Should be ready
        print('客户端 [%s:%s] 建立连接'% (addr[0],addr[1]))
        self.host_dict[conn] = addr
        self.queue_dict[conn] = queue.Queue(0)
        conn.setblocking(False)
        self.sel.register(conn, selectors.EVENT_READ, self.read)

    def read(self,conn, mask):
        try:
            data = conn.recv(4096)  # Should be ready
            if data:
                self.queue_dict[conn].put(data)
                # print(self.queue_dict[conn])
            else:
                self.sel.unregister(conn)
                del self.queue_dict[conn]
                conn.close()
                print(self.host_dict[conn][0]+':'+self.host_dict[conn][1],'客户端连接断开')
        except Exception:
            self.sel.unregister(conn)
            del self.queue_dict[conn]
            conn.close()
            print(self.host_dict[conn][0]+':'+self.host_dict[conn][1],'客户端连接断开')



    def run(self):
        sock = socket.socket()
        sock.bind(('localhost', 9998))
        sock.listen(100)
        sock.setblocking(False)
        self.sel.register(sock, selectors.EVENT_READ, self.accept)   #有新连接之后调用accept函数

        while True:
            events = self.sel.select()
            for key, mask in events:
                callback = key.data   #调用read方法
                callback(key.fileobj, mask)  #为read方法传递conn
            for conn in self.queue_dict.keys():
                # print('key1',conn)
                try:
                    # 无阻塞的向队列中get任务，当队列为空时，不等待，而是直接抛出empty异常，重点是理解block=False
                    data = self.queue_dict[conn].get_nowait()
                    # print('data',data)
                except queue.Empty as e:
                    continue
                data_dict = json.loads(data.decode())
                if hasattr(self, 'cmd_%s' % data_dict['action']):
                    func = getattr(self, 'cmd_%s' % data_dict['action'])
                    func(conn, data_dict)
                else:
                    conn.send(b'cmd invalid...')    # 命令错误


if __name__ == '__main__':
    ft = Selectros_ftp()
    ft.run()