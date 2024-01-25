import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("127.0.0.1",12345)
client_socket.connect(server_address)
message="Hello server!"
client_socket.send(message.encode('utf-8'))
data=client_socket.recv(1024)
print(f"Received data {data.decode('utf-8')}")
client_socket.close()