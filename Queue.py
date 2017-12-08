class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add(self, item):
        """ Adds new item to the beginning of python list - O(n)"""
        return self.items.insert(0, item)

    def remove(self):
        """Removes last item from the list - O(1)"""
        return self.items.pop()

    def peek(self):
        return self.items[self.size()-1]

    def size(self):
        return len(self.items)


q = Queue()
q.add(1)
q.add(30)
q.add(400)
q.add(5)
print q.peek()
q.size()

print(q.size())