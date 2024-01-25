import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("127.0.0.1",12345)
server_socket.bind(server_address)
server_socket.listen(4)
print("Connecting server")
client_socket,client_address=server_socket.accept()
print(f"Recieved data from {client_address}")
data=client_socket.recv(1024)
response="Hello Client!"
client_socket.send(response.encode('utf-8'))
client_socket.close()
server_socket.close()