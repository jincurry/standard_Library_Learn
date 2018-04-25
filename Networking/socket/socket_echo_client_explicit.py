import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_name = sys.argv[1]
server_address = (server_name, 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)


try:
    message = b'This is the message, it will be repeated'
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
