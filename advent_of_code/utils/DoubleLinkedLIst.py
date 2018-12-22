class DoubleLinkedList:
    def __init__(self, value):
        self.prev = self
        self.next = self
        self.value = value

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def get_value(self):
        return self.value

    def move_clockwise(self, steps=1):
        node = self
        for i in range(steps):
            node = node.get_next()
        return node

    def move_counter_clockwise(self, steps=1):
        node = self
        for i in range(steps):
            node = node.get_prev()
        return node

    def insert_node(self, node):
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node

    def remove_node(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.next
