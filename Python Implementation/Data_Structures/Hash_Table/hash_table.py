class HashTable:
    def __init__(self):
        self.MAX = 30
        self.arr = [[] for i in range(self.MAX)]

    def hash_code(self, key):
        CONSTANT_HASH = 31
        char_pos = 0
        hash = 0

        for char in key:
            hash += CONSTANT_HASH * char_pos + ord(char)
            char_pos += 1

        return hash % self.MAX
    
    # sets a value into a hash code for a key (ex: t['march'] = 30)
    def __setitem__(self, key, val):
        hash = self.hash_code(key)
        found = False

        for idx, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash][idx] = (key, val)
                found = True
                break
            
        if not found:
            self.arr[hash].append((key, val))
    
    # returns a values of a given key (ex: t['march'])
    def __getitem__(self, key):
        hash = self.hash_code(key)

        for element in self.arr[hash]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        hash = self.hash_code(key)

        for idx, element in enumerate(self.arr[hash]):
            if element[0] == key:
                del self.arr[hash][idx]

    def __str__(self):
        return str(self.arr)



table = HashTable()
table['march 6'] = 130
table['march 17'] = 90
table['march 8'] = 130
table['march 9'] = 90
print(table)
del table['march 9']
table['march 6'] = 50
print(table)
# while True:
#     print(table.hash_code(input("Enter a word:")))
del table
