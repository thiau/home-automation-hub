import socket


def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s


def get_ip_address():
    connection = connect()
    ip_address = connection.getsockname()[0]
    connection.close()
    return ip_address
