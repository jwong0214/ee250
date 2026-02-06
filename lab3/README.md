# Lab 3

## Team Members
- Janessa Techathamawong

## Lab Question Answers

1. How did the reliability of UDP change when you added 50% loss to your local environment? Why did this occur?
After adding 50% loss to the local environment, the reliability of UDP decreased significantly. Many packets were lost before reaching the receiver.
In our case, no data is received by the server.
This is because UDP is an unreliable protocol, and when packets are dropped by the network, UDP does not detect the loss.

2. How did the reliability and speed of the TCP response change? Why might this happen?
When the packet loss was introduced, the reliability of the TCP response remained high, but the speed of the response decreased. But it will still deliver the data without loss or corruption.
With packet loss, TCP remains reliable because it retransmits lost packets, but the response becomes slower due to these retransmissions, reducing the sending rate.

## tpc_server.c Answers

1. What is argc and *argv[]?
argc stands for argument count, and stores the number of command-line arguments passed to a program, like in a terminal. argv[] stands for argument vector, and is an array of pointers to strings that stores said command-line arguments.

2. What is a UNIX file descriptor and file descriptor table?
A UNIX file descriptor is a small integer that uniquely identifies an open file, socket, or device in a process. A UNIX file descriptor table is a per-process table maintained by the OS that maps file descriptors (0, 1, 2, 3, …) to actual open files or sockets.
In this program, sockfd and newsockfd are file descriptors referring to sockets.

3. What is a struct? What’s the structure of sockaddr_in?
A struct is a user-defined data type in C that groups related variables together. struct sockaddr_in is used to store IPv4 socket address information.
Within sockaddr_in, we have the following fields:
sin_family:  address family (e.g. AF_INET)
sin_addr.s_addr: IP address
sin_port: port number (in network byte order)

4. What are the input parameters and return value of socket()?
In the function prototype int socket(int domain, int type, int protocol);, the input parameters are as follows:
domain: address family (e.g. AF_INET)
type: socket type (e.g. SOCK_STREAM for TCP)
protocol: protocol (usually 0 to choose default)
The return values are as follows:
A file descriptor for the socket on success
-1 on failure

5. What are the input parameters of bind() and listen()?
In the function prototype int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen);, the input parameters are as follows:
sockfd: socket file descriptor
addr: pointer to address structure (sockaddr_in)
addrlen: size of the address structure
In the function prototype int listen(int sockfd, int backlog);, the input parameters are as follows:
sockfd: socket file descriptor
backlog: maximum number of pending connections allowed

6. Why use while(1)? Based on the code below, what problems might occur if there are multiple simultaneous connections to handle?
while(1) keeps the server running indefinitely, allowing it to accept connections continuously.
If there are multiple simultaneous connections that need to be handled, because this server is single-threaded and blocking, each client must finish before the next client is handled and if one client is slow or stalls, all others must wait, leading to poor scalability and dropped or delayed connections.

7. Research how the command fork() works. How can it be applied here to better handle multiple connections?
fork() creates a new child process that is a copy of the parent. After using fork(), the parent continues accepting new connections and the child handles communication with the connected client.
Here, you can call fork() after accept(), so the child process handles read()/write() and the parent immediately goes back to accept(), allowing for multiple clients to be handled concurrently.