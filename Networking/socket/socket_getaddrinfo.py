import socket


def get_constants(prefix):
    return {
        getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)
    }


families = get_constants('AF_')
types = get_constants('SOCk_')
protocols = get_constants('IPPROTO_')


for response in socket.getaddrinfo('www.python.org', 'http'):
    family, sockettype, proto, canonname, sockaddr = response

    print('Family       :', families[family])
    print('Type       :', types[sockettype])
    print('Protocol       :', protocols[proto])
    print('Canonical name       :', canonname)
    print('Socket address       :', sockaddr)
    print()

