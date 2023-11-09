import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.0.2.15", 1235))

full_msg = b''
while True:
    msg = s.recv(3)
    if len(msg) <= 0:
        break
    full_msg += msg
    print(full_msg.decode("utf-8"))
