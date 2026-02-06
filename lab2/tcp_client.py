"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    # TODO: Get user input and send it to the server using your TCP socket
    # TODO: Receive a response from the server and close the TCP connection
    # pass

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = '192.169.0.141'
    server_port = 5000
    client_socket.connect((server_ip, server_port))

    message = input("input-> ")

    client_socket.send(message.encode())

    response = client_socket.recv(256)
    print("Server says:", response.decode())

    client_socket.close()

if __name__ == '__main__':
    main()

