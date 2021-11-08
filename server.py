import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 4567))

s.listen(10)

while True:
  clientsocket, address = s.accept()
  print(f"Connection from {address} has been established.")
  clientsocket.send(bytes("Welcome","utf-8"))
