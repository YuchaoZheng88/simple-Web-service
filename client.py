import socket
import json

ServerIp='127.0.0.1'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ServerIp, 1234))

a = input("First hex: ")
b = input("Operator: ")
c = input("Second hex: ")

d = "0x{:x}".format(int(a,16))
e = "0x{:x}".format(int(c,16))

data = json.dumps({"a": a, "b": b, "c": c, "d": d, "e": e})
s.sendto(data.encode(),0,(ServerIp, 1234))

msg = s.recv(1024)
if(msg):
    print(msg.decode("utf-8"))
