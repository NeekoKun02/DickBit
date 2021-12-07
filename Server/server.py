import json, socket
from hashmap import HashMap

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
index = HashMap().add(json.load(open('./Server/numbers_ips.py')))
pakage, ip = s.recvfrom()      # pakage = (<sender>, <type>, (<receiver>, <msgContent>))

################################################################################################
################################################################################################

def send(pkg):
    

################################################################################################
################################################################################################

switcher={
    'msg' : sendto(pakage)
}

switcher.get(pakage[0], error(pakage))