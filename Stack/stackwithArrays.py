class stackList:
    def __init__(self):
        self._stack = []
        
    def size(self):
        return len(self._stack)

    def isEmpty(self):
        return len(self._stack)==0

    def push(self,val):
        self._stack.append(val)

    def pop(self):
        if self.isEmpty():
            print("stacks is empty")

        else:
            self._stack.pop()
    def peek(self):
        return self._stack[-1]

    def display(self):
        for i in self._stack:
            print(i, end="-->")
        print()

sl = stackList()
sl.push(20)
sl.push(30)
sl.display()
sl.pop()
sl.display()

    