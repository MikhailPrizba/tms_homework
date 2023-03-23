import socket
from dotenv import dotenv_values
from views import calculate



def start_server():
    config = dotenv_values('./.env')['SOCKET_ADDRES']
    host = config.split(':')[0]
    port = int(config.split(':')[-1])
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print('working')
    client_socket, address = server.accept()
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(data)
        content = calculate(data).encode('utf-8')
        client_socket.sendall(content)

start_server()