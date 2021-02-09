import socket


def get_hostname():
    return socket.gethostname()


def get_ip_address():
    hostname = get_hostname()
    return socket.gethostbyname(hostname)
