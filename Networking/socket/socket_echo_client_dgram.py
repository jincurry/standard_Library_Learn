import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'This is the message, it will be repeated'

try:
    print('Sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)
    print('Waiting for receive')
    data, server = sock.recvfrom(4096)
    print('Received {!r}'.format(data))

finally:
    print('Closing socket')
    sock.close()
