import json, socket
from hashmap import HashMap

global SERVER_IP
SERVER_IP = '25.77.61.44'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
index = HashMap().add(json.load(open('./Server/numbers_ips.py')))
pakage, ip = s.recvfrom()      # pakage = (<sender>, <type>, (<receiver>, <msgContent>))

################################################################################################
################################################################################################

def send(pkg, ip):
    try:
        sender = list(index.keys())[list(index.values()).index(ip)]
        s.sendto((sender, 'msg', pkg[2][1]), (index.get(pkg[2][0])))
    except ValueError:
        s.sendto((SERVER_IP, 'error', '0x00101').encode('utf-8'), (ip, 12345))

    

################################################################################################
################################################################################################

switcher={
    'msg' : send(pakage.decode('utf-8'), ip)
}

switcher.get(pakage[0], error(pakage))