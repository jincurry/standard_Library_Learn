import sys
import socketserver


class Echo(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        self.request.send(data)
        return


if __name__ == '__main__':
    import codecs
    import socket
    import threading

    address = ('localhist', 0)
    server = socketserver.TCPServer(address, Echo)
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(ip, port)

    text = 'français'
    len_sent = s.send(text)

    response = s.recv(len_sent)
    print(repr(response))

    s.close()
    server.socket.close()
