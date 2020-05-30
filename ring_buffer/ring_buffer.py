class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = [None] * capacity
        self.oldest_element = 0

    def append(self, item):
        self.store.[self.oldest_element] = item

    def get(self):
        pass