class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.current >= self.capacity:
            self.current = 0
        self.storage[self.current] = item
        self.current += 1

    def get(self):
        if None in self.storage:
            return [item for item in self.storage if item != None]
        else:
            return self.storage
