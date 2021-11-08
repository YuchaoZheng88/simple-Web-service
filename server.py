import socket
import json

ServerIp='127.0.0.1'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ServerIp, 1234))

s.listen(10)

while True:
  clientsocket, address = s.accept()
  print("Connection from {address} has been established.")
  clientsocket.send(bytes("Welcome","utf-8"))

  data = clientsocket.recv(1024)
  data = json.loads(data.decode())
  arr = data.get("a")
  var = data.get("c")
  print(arr)
  print(var)
