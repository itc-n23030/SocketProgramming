import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("10.0.2.15", 1235))  # IPとポート番号を指定します
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("こんにちは", 'utf-8'))
    clientsocket.close()
