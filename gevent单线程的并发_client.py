# import socket
#
# HOST = 'localhost'  # The remote host
# PORT = 8001  # The same port as used by the server
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# while True:
#     msg = bytes(input(">>:"), encoding="utf8")
#     s.sendall(msg)
#     data = s.recv(1024)
#     # print(data)
#
#     print('Received', repr(data))
# s.close()




import socket
import threading

def sock_conn():

    client = socket.socket()

    client.connect(("localhost",8001))
    count = 0
    while True:
        #msg = input(">>:").strip()
        #if len(msg) == 0:continue
        client.send( ("hello %s" %count).encode("utf-8"))

        data = client.recv(1024)

        print("[%s]recv from server:" % threading.get_ident(),data.decode()) #结果
        count +=1
    client.close()


for i in range(100):
    t = threading.Thread(target=sock_conn)
    t.start()