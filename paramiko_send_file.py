import paramiko

def ssh_conn(ip):
    with paramiko.SSHClient() as client:#连接远程主机
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client.connect('192.168.10.67',22,'root','root')

        stdin,stdout,stderr = client.exec_command('ls -l') #执行命令
        print(stdout.readlines())

    with client.open_sftp() as trans:#上传文件并修改权限
        trans.put('/home/vfast/sql-dump.sql','sql-dump.sql')
        trans.chmod('sql-dump.sql',0o755)

def main():
    with open('hosts.txt','r') as f: #遍历主机ip
        for ip in f:
            ssh_conn(ip.strip())

if __name__ == '__main__':
    main()
