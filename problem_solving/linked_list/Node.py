class Node:
    __slots__ = ['value', 'next']

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def set_value(self, value):
        self.value = value

    def get_value(self, value):
        return self.value

    def set_next(self, next):
        self.next = next

    def get_next(self, next):
        return self.next

    def __str__(self):
        return self.value
