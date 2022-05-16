#hash_map


#iterates over characters of a string, and sums the ASCII values of each character
def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)  #ord gives you ASCII value
    return h % 100    #100 is the size of list


class HashTable:
    def __init__(self):
        self.MAX = 100    #100 elements initially
        self.arr = [None for i in range(self.MAX)]   #each value is none

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)  #ord gives you ASCII value
        return h % self.MAX    #100 is the size of list

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]


t = HashTable()
t.get_hash('march 6')   #returns ASCII value, 9
#t.add('march 6', 130)   #for key 'march 6', the value is now '130', the value '130' is placed at index 9
t['dec 6'] = 27
t['march 6']
print(t['dec 6'])
