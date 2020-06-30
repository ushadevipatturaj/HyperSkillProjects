class Stack():

    def __init__(self):
        self.elements = []

    def push(self, el):
        self.elements.append(el)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[len(self.elements) - 1]

    def is_empty(self):
        return len(self.elements) == 0

st1 = Stack()
print(st1.is_empty())
print(st1.push(0))
print(st1.push(1))
print(st1.push(2))
print(st1.push(3))
print(st1.push(4))
print(st1.pop())
print(st1.pop())
print(st1.peek())
print(st1.pop())
print(st1.is_empty())