import json

class HashMap:
    def __init__(self):
        self.size = 64
        self.map = [None] * self.size

    def _get_hash(self, ip):
        hash = 0

        for char in str(ip):
            hash += ord(char)
        return hash % self.size

    def add(self, ip, number):
        ip_hash = self._get_hash(ip)
        ip_number = [ip, number]

        if self.map[ip_hash] is None:
            self.map[ip_hash] = list([ip_number])
            return True
        else:
            for pair in self.map[ip_hash]:
                if pair[0] == ip:
                    pair[1] = number
                    return True
                else:
                    self.map[ip_hash].append(list([ip_number]))
                    return True

    def get(self, ip):
        ip_hash = self._get_hash(ip)
        if self.map[ip_hash] is not None:
            for pair in self.map[ip_hash]: 
                if pair[0] == ip:
                    return pair[1]
        return None

    def delete(self, ip):
        ip_hash = self._get_hash(ip)

        if self.map[ip_hash] is None :
            return False
        for i in range(0, len(self.map[ip_hash])):
            if self.map[ip_hash][i][0] == ip:
                self.map[ip_hash].pop(i)
                return True

    def print(self):

        print('---NUMBERS & IPS---')
        for item in self.map:
            if item is not None:
                print(str(item))