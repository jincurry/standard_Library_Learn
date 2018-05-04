import socket
import sys
import os

server_address = './uds_socket'

try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

print('starting up on {}'.format(server_address))
socket.bind(server_address)

socket.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = socket.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break
    finally:
        connection.close()
