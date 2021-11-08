import socket

####################
import json


arr1 = [1,2,3]
arr2 = [4,5,6]
someVar = 7
data = json.dumps({"a": arr1, "b": arr2, "c": someVar})

#########################
ServerIp='127.0.0.1'


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ServerIp, 1234))

##
s.sendto(data.encode(),0,(ServerIp, 1234))

msg = s.recv(1024)
print(msg.decode("utf-8"))
