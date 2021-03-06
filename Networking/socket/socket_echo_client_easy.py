import socket
import sys


def get_constants(prefix):

    return {
        getattr(socket, n) : n
        for n in dir(socket)
        if n.startswith(prefix)
    }


families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

sock = socket.create_connection(('localhost', 10000))

print('Family :', families[sock.family])
print('Type :', types[sock.type])
print('Protocol:', protocols[sock.proto])

try:
    message = b'this is the message, it will be repeated'
    print('Sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))
finally:
    print('Closing socket')
    sock.close()
