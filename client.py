import socket

ServerIp=127.0.0.1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ServerIp, 4567))

msg = s.recv(1024)
print(msg.decode("utf-8"))
