from collections import deque


class RingBuffer:
    def __init__(self, capacity):
        #define a fixed size
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
            #self.storage.rotate(self.capacity - self.neg_count)
            self.storage.popleft()
            self.storage.append(item)
            


    def get(self):
        return list(self.storage)

if __name__ == '__main__':

    ring = RingBuffer(5)
    for i in range(50):
        ring.append(i)
        print(ring.get())
