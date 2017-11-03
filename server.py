import socket
HOST = '172.17.0.2'
PORT = 2001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print("Server start at: %s/:%s" %(HOST,PORT))
print("Waiting for connection...")

while True:
    conn, addr = s.accept()
    print("Connect by ", addr)

    while True:
        data = conn.recv(1024)
        print(data.decode('utf-8'))
        conn.send("server has received your message.".encode('utf-8'))
