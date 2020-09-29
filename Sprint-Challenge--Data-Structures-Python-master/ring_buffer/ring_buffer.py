from collections import deque


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = deque(maxlen=self.capacity)
        self.neg_count = 1
        self.pos_count = 0


    def append(self, item):
        if self.capacity == (self.neg_count - 1):
            self.neg_count = 1
            self.pos_count = 0

        #if ring buffer is not full
        if len(self.storage) < self.capacity:
            self.storage.append(item)

        #ring buffer is full
        elif self.capacity == len(self.storage):
            self.storage.rotate(self.capacity - self.neg_count)
            self.storage.append(item)
            self.storage.rotate(self.capacity + self.pos_count)
            self.neg_count = self.neg_count + 1
            self.pos_count = self.pos_count + 1


    def get(self):
        return list(self.storage)

if __name__ == '__main__':
    x = RingBuffer(5)
    x.append(1)
    x.append(2)
    x.append(3)
    x.append(4)
    print(x.get())
