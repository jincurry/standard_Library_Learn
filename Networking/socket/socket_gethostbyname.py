import socket


HOSTS = [
    'jincurry.githuob.io',
    'pymotw.com',
    'www.python.org',
    'nosuchname',
]


for host in HOSTS:
    try:
        print('{} : {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{}: {}'.format(host, msg))
