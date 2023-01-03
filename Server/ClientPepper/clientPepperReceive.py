import socket
import sys
import os
import struct




#host = input("ENTER SERVER IP (format 123.456.789.123)\n")
host = "localhost"
port = 39039
try:
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_socket.connect((host, port))
    print("Connected to {} using port {}".format(host,port))
    msg= b"setname PepperReceive"
    size = len(msg)

    main_socket.send(struct.pack("!H", size))
    main_socket.send(msg)
    msg_in = main_socket.recv(1024).decode('utf-8')
    print(msg_in[2:])
except OSError:
    print("[Erreur] Timeout\nVérifier que le serveur est bien démarré et réessayer !")
    os.system("pause")
    sys.exit()


Ack = b'ack'
sizeAck = len(Ack)


msg_in = b""
while not (msg_in == b"stop" or msg_in == b"disconnect"):
    msg_in = ""    
    msg_in = main_socket.recv(1024).decode('utf-8')
    print(msg_in[2:])

print("[INFO] Closing connection")
main_socket.close()
