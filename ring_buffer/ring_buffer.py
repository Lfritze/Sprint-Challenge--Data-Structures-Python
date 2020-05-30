class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = [None] * capacity
        self.oldest_element = 0

    def append(self, item):
        self.store[self.oldest_element] = item

        if self.oldest_element == self.capacity - 1:
            self.oldest_element = 0
        else:
            self.oldest_element += 1

    def get(self):
        return [item for item in self.store if item is not None]