import socket
import json

ServerIp='127.0.0.1'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ServerIp, 1234))

s.listen(10)

while True:
  clientsocket, address = s.accept()
  print("Connection from {address} has been established.".format(address=address))

  data = clientsocket.recv(1024)
  data = json.loads(data.decode())
  a = data.get("a")
  b = data.get("b")
  c = data.get("c")
  d = data.get("d")
  e = data.get("e")
  print(a)
  print(b)

  result = ""

  if (b == "+" or b == "add"):
    g = "0x{:x}".format(int(d,16)+int(e,16))
    result = "\nThe result of adding "+d+" and "+e+" is: "+g+"\n"
  elif (b == "-" or b == "sub"):
    g = "0x{:x}".format(int(d,16)-int(e,16))
    result = "\nThe result of subtracting "+d+" and "+e+" is: "+g+"\n"
  elif (b == "mul" or b == "*"):
    g = "0x{:x}".format(int(d,16)*int(e,16))
    result = "\nThe result of multiplying "+d+" and "+e+" is: "+g+"\n"
  elif (b == "div" or b == "/"):
    g = "0x{:x}".format(int(d,16)/int(e,16))
    result = "\nThe result of dividing "+d+" and "+e+" is: "+g+"\n"
  else:
    result = "Error Input!"

  print(result + "to the address: {address}".format(address=address))
  clientsocket.send(bytes(result,"utf-8"))
