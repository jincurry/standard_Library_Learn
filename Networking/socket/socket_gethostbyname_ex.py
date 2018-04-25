import socket


HOSTS = [
    'jincurry.github.io',
    'pymotw.com',
    'www.python.org',
    'nosuchname',
]


for host in HOSTS:
    print(host)
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print(' Hostname:', name)
        print(' Aliases:', aliases)
        print(' Addresses:', addresses)
    except socket.error as msg:
        print('Error:', msg)
    finally:
        print()
