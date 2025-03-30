import socket
import jsonpickle

IP = "127.0.0.1"
PORT = 4000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)
conn, addr = server.accept()
data = b""
while True:
    packet = conn.recv(1024)
    if not packet: break
    data += packet
listOfProc = jsonpickle.decode(data.decode())
for proc in listOfProc:
    print(proc)
conn.close()
server.close()