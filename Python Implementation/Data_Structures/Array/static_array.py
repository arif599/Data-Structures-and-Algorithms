class StaticArray:
    def __init__(self, size):
        self.arr = [0 for i in range(size)]
        self.size = size
        self.indexCounter = 0

    def append(self, element):
        self.arr[self.indexCounter] = element
        self.indexCounter += 1

    def insert(self, index, element):
        if self.indexCounter < self.size:
            counter = 0
            for i in range(index, self.size):
                if self.arr[i] == 0:
                    self.arr[i] = self.arr[i-counter+1]
                else:
                    counter += 1

    
    def print(self):
        for i in range(self.size):
            print(self.arr[i], end=" ")

if __name__ == "__main__":
    array = StaticArray(5)
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(5)
    array.print()
    array.insert(3, 4)
    array.print()