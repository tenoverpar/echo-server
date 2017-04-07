import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

address = ('127.0.0.1', 20000)

server_socket.bind(address)
server_socket.listen(1)

connection, client_address = server_socket.accept()

buffer_size = 4096
received_message = connection.recv(buffer_size)

print("Client says: {}".format(received_message.decode()))

connection.sendall("message received".encode('utf8'))

