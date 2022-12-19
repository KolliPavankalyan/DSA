class _Node:
    __slots__ = "_element", "_next"
    def __init__(self, element, next):
        self._element = element
        self._next = next

class queueLinkedList:
    def __init__(self):
        self._front = None
        self._rare = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return len(self) == 0

    def enqueue(self, val):
        newNode = _Node(val, None)
        if self._front == None:
            self._front = newNode
            self._rare = newNode
        else:
            self._rare._next = newNode
            self._rare = newNode
        self._size += 1

    def dequeue(self):
        r = None
        if self.isempty():
            print("Queue is empty!...")
        else:
            r = self._front._element
            self._front = self._front._next
            self._size -= 1
        return r

    def first(self):
        val = None
        if self.isempty():
            print("Queue is empty!...")
        else:
            val  = self._front._element
        return val

    def display(self):
        temp = self._front
        while temp:
            print(temp._element, end ="<--" )
            temp = temp._next
        print()

Qll = queueLinkedList()
Qll.enqueue(10)
Qll.enqueue(20)
Qll.enqueue(30)
Qll.enqueue(40)
Qll.enqueue(50)
Qll.display()
Qll.dequeue()
Qll.display()
