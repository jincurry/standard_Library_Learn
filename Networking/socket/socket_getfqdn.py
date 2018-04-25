import socket


for host in ['jincurry.github.io', 'pymotw.com', 'www.zhihu.com', 'www.python.org']:
    print('{:>10} : {}'.format(host, socket.getfqdn(host)))
