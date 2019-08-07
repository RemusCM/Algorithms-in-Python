#stack implementation in python.

class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return list(reversed(self.items))

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Empty"

s = Stack()
print(s.get_stack())
s.push("A")
s.push("B")
print(s.get_stack())
s.pop()
print(s.get_stack())
