import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address=("localhost",12345)
while True:
    message=input("Enter message")
    client_socket.sendto(message.encode(),server_address)
client_socket.close()