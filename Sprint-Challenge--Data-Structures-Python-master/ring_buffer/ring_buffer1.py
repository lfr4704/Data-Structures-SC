from collections import deque


class RingBuffer:
    """
    class that implements a not yet full ring buffer
    """
    def __init__(self, capacity):
        #define a fixed size
        self.capacity = capacity
        self.data = []

        class __Full:
            """
            class that implements a full ring buffer
            """
            def append(self, x):
                """append an element that overwritest the lastest one
                afer capacity has been reached
                """
                #define the first item in list
                self.data[self.curr] = x
                self.curr = (self.curr + 1) % self.capacity

                def get(self):
                    """
                    returns elements in correct order
                    """
                    return self.data[self.curr:] + self.data[:self.curr]
                    # Permanently change self's class from non-full to full
                    self.__class__= self.__Full

    def append(self, x):
        """append an element at the end of buffer"""
        self.data.append(x)
        if len(self.data) == self.capacity:
            self.curr = 0

    def get(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data

# sample usage
if __name__=='__main__':
    x=RingBuffer(5)
    x.append(1); x.append(2); x.append(3); x.append(4)
    print(x.get())
    x.append(5)
    print(x.get())
    x.append(6)
    print(x.data, x.get())
    x.append(7); x.append(8); x.append(9); x.append(10)
    print(x.data, x.get())
