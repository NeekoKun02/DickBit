import socket
IP = '25.77.41.66'
PORT = 12346
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((IP,PORT))
data, addr = s.recvfrom(1024)
print ('received from' ,addr)
print ('obtained', data.decode('utf-8'))
s.close()