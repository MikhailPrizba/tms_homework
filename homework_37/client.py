import socket
from dotenv import dotenv_values

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    config = dotenv_values('./.env')['SOCKET_ADDRES']
    host = config.split(':')[0]
    port = int(config.split(':')[-1])
    sock.connect((host, port))
    while True:
        data = input('Type message: ')
        data_b = data.encode('utf-8')
        sock.sendall(data_b)
        data_b = sock.recv(1024)
        data = data_b.decode('utf-8')
        print(data)

client()