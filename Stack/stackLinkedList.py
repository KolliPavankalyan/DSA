class _Node:
    __slots__ = '_element','_next'
    def __init__(self,element,next):
        self._element = element
        self._next = next


class stackLinkedlist:
    def __init__(self):
        self._top = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def isEmpty(self):
        return len(self)==0

    def push(self,val):
        newNode = _Node(val,None)
        if self.isEmpty():
            self._top = newNode
        else:
            newNode._next = self._top
            self._top = newNode
        self._size +=1

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            self._top = self._top._next
        self._size -=1
    
    def peek(self):
        return self._top._element

    def display(self):
        temp = self._top
        while temp:
            print(temp._element, end = "-->")
            temp = temp._next
        print()

stack = stackLinkedlist()
stack.push(20)
stack.push(30)
stack.display()
stack.push(40)

stack.pop()
stack.display()
print(stack.peek())
