import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
client_socket.connect(("127.0.0.1", 20000))

my_message = input("> ")
client_socket.sendall(my_message.encode('utf-8'))

received_message = client_socket.recv(4096)
print("Server says: {}".format(received_message.decode()))

client_socket.close()
