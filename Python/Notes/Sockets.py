#SOCKETS------------------------------------------------------------

import socket
HOST = '127.0.0.1' #af_inet
PORT = 7777 #sock_stream

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is IPv4, sock_stream is a port

s.connect((HOST,PORT))