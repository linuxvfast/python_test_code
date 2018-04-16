import socket

client = socket.socket()
client.connect(('localhost',9999))
while True:
    msg = input('>>').strip()
    client.send(msg.encode())
    data = client.recv(1024)
    print(data)

client.close()