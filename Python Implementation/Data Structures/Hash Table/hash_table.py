class HashTable:
    def __init__(self):
        self.MAX = 30
        self.arr = [None for i in range(self.MAX)]

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
        self.arr[self.hash_code(key)] = val
    
    # returns a values of a given key (ex: t['march'])
    def __getitem__(self, key):
        return self.arr[self.hash_code(key)]

    def __delitem__(self, key):
        self.arr[self.hash_code(key)] = None

    def __str__(self):
        return str(self.arr)



table = HashTable()
table['march 6'] = 130
print(table['march 6'])
print(table)
# while True:
#     print(table.hash_code(input("Enter a word:")))
del table
