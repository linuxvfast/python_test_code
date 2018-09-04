from socket import *

def conn_scan(host,port):
    conn = socket(AF_INET, SOCK_STREAM)
    try:
        conn.connect((host,port))
        print(host,port,'is alive')
    except Exception as e:
        print(host,port,'is down')
    finally:
        conn.close()



def main():
    host = '192.168.10.75'
    for port in [22,80,3306,8080]:
        conn_scan(host,port)



if __name__ == '__main__':
    main()


#使用telnet测试
# import telnetlib
#
# def conn_scan(host,port):
#     t = telnetlib.Telnet()
#     try:
#         # t.open(host,port,timeout=1)
#         t.open(host,port)
#         print(host,port,'is alive')
#     except Exception as e:
#         print(host,port,'is down')
#     finally:
#         t.close()
#
# def main():
#     host = '192.168.10.75'
#     for port in [22,80,3306,8080]:
#         conn_scan(host,port)
#
# if __name__ == '__main__':
#     main()
