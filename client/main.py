import socket
import jsonpickle
import psutil

IP = "127.0.0.1"
PORT = 4000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
data = jsonpickle.encode(list(psutil.process_iter()), indent=4).encode()
for i in range(0, len(data), 1024):
    client.send(data[i:i+1024])
client.close()