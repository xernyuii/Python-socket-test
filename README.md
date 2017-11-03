# Python-socket-test
Based on 2 docker containers
Send messages between two docker containers by Python.socket
## code preview
### server on 127.0.17.2
```python
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

```
### client on 127.0.17.3
```python
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

```

## docker_info
```
"Containers": {
    "6526836965e3d607ea88c0d075d4ae376f7bc4742e17fe7b055691130bd24933": {
        "Name": "client",
        "MacAddress": "02:42:ac:11:00:03",
        "IPv4Address": "172.17.0.3/16",
        "IPv6Address": ""
    },
    "7c58163e6353871d4c1e9bb5f7e6de6e71a43d4ee0deba7a25f89041f442936f": {
        "Name": "server",
        "MacAddress": "02:42:ac:11:00:02",
        "IPv4Address": "172.17.0.2/16",
        "IPv6Address": ""
    }
},
```

## examples

### server on 127.0.17.2
![](https://raw.githubusercontent.com/xernyuii/Python-socket-test/master/examples/server_on_02.png)

### client on 127.0.17.3
![](https://raw.githubusercontent.com/xernyuii/Python-socket-test/master/examples/client_on_03.png)
