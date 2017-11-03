import socket
HOST = '172.17.0.2'
PORT = 2001

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    cmd = input("Send message:")
    s.send(cmd.encode("utf-8"))
    data = s.recv(1024)
    print(data.decode('utf-8'))
