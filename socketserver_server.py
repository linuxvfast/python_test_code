__author__ = 'progress'

import socketserver

class Mytcphandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print('{} wrote:'.format(self.client_address[0]))
                print(self.data)
                self.request.sendall(self.data.upper())
            except ConnectionResetError as e:
                print(self.client_address,'exit...')
                break

if __name__ == '__main__':
    HOST,PORT = 'localhost',9999
    # server = socketserver.TCPServer((HOST,PORT),Mytcphandler)
    server = socketserver.ThreadingTCPServer((HOST,PORT),Mytcphandler)
    server.serve_forever()


