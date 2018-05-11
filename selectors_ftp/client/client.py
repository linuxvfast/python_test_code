import socket
import os
import sys
import json
import base64


class FTPClient(object):
    def __init__(self):
        self.default_save_path = None
        self.client = socket.socket()
        self.connect()

    def connect(self):
        profile_dict = json.load(open('profile', 'r', encoding='utf-8'))
        self.default_save_path = profile_dict['default_save_path']
        self.client.connect((profile_dict['host'], int(profile_dict['port'])))

    @staticmethod
    def configure(): #保存ip和端口已经客户端目录
        host = input('主机IP或主机名：').strip()
        port = input('端口：').strip()
        default_save_path = input('默认下载目录：').strip()
        host_info = {
            'host': host,
            'port': port,
            'default_save_path': default_save_path
        }
        f = open('profile', 'w', encoding='utf-8')
        json.dump(host_info, f)
        f.close()

    @staticmethod
    def help():
        print("""
        --------------------help info--------------------
                说明：上传文件需填写文件绝对路径，下载文件只支持保存到默认下载路径
                上传文件：put path/filename
                下载文件：get filename 
        """)

    def interactive(self):
        while True:
            cmd = input('\033[34;1m>>>\033[0m').strip()
            if not cmd:
                continue
            if hasattr(self, 'cmd_%s' % cmd.split()[0]):
                func = getattr(self, 'cmd_%s' % cmd.split()[0])
                func(cmd)
            else:
                self.help()

    @staticmethod
    def progress_bar(percent):
        percent = int(percent)
        s1 = "\r【\033[34;1m%s%s\033[0m%s】%d%%" % ("-" * percent, '✈', '-' * (100 - percent), percent)
        sys.stdout.write(s1)
        sys.stdout.flush()

    def cmd_get(self, cmd):
        if len(cmd.split()) < 2:
            self.help()
            return
        download_file = os.path.join(self.default_save_path, cmd.split()[-1])
        data = {
            'action': 'get',
            'filename': cmd.split()[-1]
        }
        self.client.sendall(json.dumps(data).encode('utf-8'))
        res = json.loads(self.client.recv(1024).decode())
        if res['action'] == 'ERROR':
            if res['code'] == '401':
                print('服务端：文件不存在')
                return
        file_size = int(res['size'])
        file_size_tmp = 0
        f = open(download_file, 'wb')
        data1 = {
            'action': 'read'
        }
        while file_size_tmp < file_size:
            self.client.sendall(json.dumps(data1).encode('utf-8'))
            data = self.client.recv(1024)
            f.write(data)
            file_size_tmp += len(data)
            percent = '%d' % (file_size_tmp / file_size * 100)
            self.progress_bar(percent)
        f.close()
        print()

    def cmd_put(self, cmd):
        if len(cmd.split()) < 2:
            self.help()
            return
        if not os.path.isfile(cmd.split()[-1]):
            print('客户端：文件不存在')
            return
        file_size = os.path.getsize(cmd.split()[-1])
        if '/' in cmd.split()[-1]:
            filename = cmd.split()[-1].split('/')[-1]
        else:
            filename = cmd.split()[-1].split('\\')[-1]
        data1 = {
            'action': 'put',
            'filename': filename,
            'size': file_size
        }
        self.client.sendall(json.dumps(data1).encode('utf-8'))
        res = self.client.recv(1024)
        if res == b'402':
            print('服务端：文件已存在')
            return
        f = open(cmd.split()[-1], 'rb')
        file_size_tmp = 0
        while True:
            data = f.read(1024)
            if not data:
                break
            data2 = {
                'action': 'write',
                'file_data': base64.b64encode(data).decode()
            }
            self.client.sendall(json.dumps(data2).encode('utf-8'))
            file_size_tmp += len(data)
            percent = '%d' % (file_size_tmp/file_size*100)
            self.progress_bar(percent)
            self.client.recv(1024)
        print()
        f.close()


if not os.path.isfile('profile'):
    print('系统初始化。。。')
    FTPClient.configure()
while True:
    print("""
    ==================FTP CLIENT==================
                       1、修改配置信息
                       2、登陆FTP服务器
                       3、退出
    """)
    choice = input('>>>').strip()
    if choice == '1':
        FTPClient.configure()
    elif choice == '2':
        client = FTPClient()
        client.interactive()
    elif choice == '3':
        exit('系统即将退出~')
    else:
        print('错误选项~')












