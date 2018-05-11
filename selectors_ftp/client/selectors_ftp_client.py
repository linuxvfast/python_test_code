import socket,os,json
# import sys
file_dir = os.path.dirname(os.path.abspath(__file__))
# print(file_dir)
# sys.path.append(file_dir)
import optparse,base64




class Ftpclient(object):
    def __init__(self):
        '''智能读取参数'''
        self.parse = optparse.OptionParser()
        self.parse.add_option('-s','--host',dest='host',help='Binding the address of the server')
        self.parse.add_option('-P','--port',type='int',dest='port',help='Binding server port')
        (self.options, self.args) = self.parse.parse_args()
        self.make_connect()

    def make_connect(self):
        '''连接服务器'''
        self.client = socket.socket()
        self.client.connect((self.options.host,self.options.port))

    def help(self):
        #命令帮助
        msg = '''
        ----------命令操作如下----------
        get  filename  下载文件
        put  filename  上传文件
        '''
        print(msg)

    def cmd_put(self,cmd_list):
        '''上传文件'''
        if len(cmd_list) < 2:
            self.help()
            return
        file_path = '%s/%s'%(file_dir,cmd_list[1])
        if not os.path.isfile(file_path):
            print('客户端：文件不存在')
            return
        file_size = os.path.getsize(file_path)
        data1 = {
            'action': 'put',
            'file_name': cmd_list[1],
            'size': file_size
        }
        self.client.send(json.dumps(data1).encode())
        print(self.client.recv(1024))
        f = open(file_path, 'rb')
        send_size = 0
        while True:
            data = f.read(1024)
            if not data:
                break

            data2 = {
                'action': 'write',
                'file_data': base64.b64encode(data).decode(),
            }
            print('data2',data2)
            self.client.sendall(json.dumps(data2).encode())
            send_size += len(data)
            # print('send_size',send_size)
            self.client.recv(1024)
        print('文件发送完成')
        f.close()

    def cmd_get(self,cmd_list):#cmd_list =[get,weblogic.txt]
        #下载文件
        if len(cmd_list) < 2:
            self.help()
            return
        download_file = os.path.join(file_dir, cmd_list[1])
        data = {
            'action': 'get',
            'file_name': cmd_list[1]
        }
        self.client.send(json.dumps(data).encode())
        res = json.loads(self.client.recv(1024).decode())
        # print('res',res)
        if res['action'] == 'Error':
            if res['code'] == '401':
                print('服务端：文件不存在')
                return
        file_size = int(res['size'])
        recv_size = 0
        f = open(download_file, 'wb')
        data1 = {
            'action': 'read'
        }
        while recv_size < file_size:
            self.client.send(json.dumps(data1).encode())
            data = self.client.recv(1024)
            f.write(data)
            recv_size += len(data)
        f.close()
        print('文件接收完成')

    def get_repsone(self):
        '''接受服务器的返回结果'''
        data = self.client.recv(1024)
        data = json.loads(data.decode())
        return data

    def interactive(self):
        #交互
        while True:
            choice = input('>>').strip()
            if len(choice) == 0:continue
            if choice == 'exit':break
            cmd_list = choice.split()
            if hasattr(self,'cmd_%s'%cmd_list[0]):
                func = getattr(self,'cmd_%s'%cmd_list[0])
                func(cmd_list)
            else:
                print('invalid cmd...')
                self.help()



if __name__ == '__main__':
    obj = Ftpclient()
    obj.interactive()
