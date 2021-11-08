import socket

ServerIp='127.0.0.1'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ServerIp, 1234))

s.listen(10)

while True:
  clientsocket, address = s.accept()
  print("Connection from {address} has been established.")
  clientsocket.send(bytes("Welcome","utf-8"))
