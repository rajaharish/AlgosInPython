class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        """ Adds new item to the end of python list - O(1)"""
        return self.items.append(item)

    def pop(self):
        """Removes last item from the list - O(1)"""
        return self.items.pop()

    def peek(self):
        """Returns last item in the list - O(1)"""
        return self.items[self.size()-1]

    def size(self):
        return len(self.items)


s = Stack()
s.push(30)
s.push(400)
s.push(5)
print(s.size())
s.pop()
s.size()

print(s.size())