import socket
import threading
from RequestParser import Request_parser

bind_ip = "127.0.0.1"
bind_port = 5000


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print(f'[*] Listening on {bind_ip}:{bind_port}')


def handle_client(client_socket):

	request = Request_parser(client_socket.recv(4096).decode())
	path, method, protocol = request.get_little_data()

	print(f'[*] {method} - {protocol} - {path}')

	client_socket.send(f'HTTP/1.0 200 OK\n\n<html><head><title>Hi</title></head><body><h1>{path}</h1></body></html>'.encode())
	client_socket.close()


def run():
	while True:
		client, addr = server.accept()
		print(f'[*] Accepted connection from: {addr[0]}:{addr[1]}')
		client_handler = threading.Thread(target=handle_client,args=(client,))
		client_handler.start()