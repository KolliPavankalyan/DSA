class _Node:
    __slots__ = "_element", "_next", "_prev"
    def __init__(self, element, next, prev):
        self._element = element
        self._next = next
        self._prev = prev

class doublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0

    def addlast(self, e):
        newNode = _Node(e, None, None)
        if self.isempty():
            self._head = newNode
            self._tail = newNode
        else:
            self._tail._next = newNode
            newNode._prev = self._tail
            self._tail = newNode
        self._size += 1
    
    def addfirst(self, e):
        newNode = _Node(e, None, None)
        if self.isempty():
            self._head = newNode
            self._tail = newNode
        else:
            newNode._next = self._head
            self._head._prev = newNode
            self._head = newNode
        self._size += 1

    def addany(self, e, position):
        if position <= 0:
            self.addfirst(e)
        elif position >= self.__len__():
            self.addlast(e)
        else:
            newNode = _Node(e, None, None)
            temp = self._head
            i = 1
            while i < position:
                temp = temp._next
                i += 1
            newNode._next = temp._next
            temp._next._prev = newNode
            newNode._prev = temp
            temp._next = newNode
            
            self._size += 1

    def removefirst(self):
        if self.isempty():
            print("Linked list is empty!..")
        else:
            self._head = self._head._next
            if self._head == None:
                self._tail = None
            else:
                self._head._prev = None
            self._size -= 1
    

    def removelast(self):
        if self.isempty():
            print("Linked list is empty!..")
        else:
            self._tail = self._tail._prev
            if self._tail == None:
                self._head = None
            else:
                self._tail._next = None
            self._size -= 1 
    
    def removeany(self, position):
        if position < 0 or position >= self.__len__():
            print("List index out of range!..")
        elif position == 0:
            self.removefirst()
        elif position == self.__len__()-1:
            self.removelast()
        else:
            temp = self._head
            i = 1
            while i < position:
                temp = temp._next
                i += 1
            temp._next._element
            temp._next = temp._next._next
            temp._next._prev = temp
            self._size -= 1


    def displayForward(self):
        temp = self._head
        while temp:
            print(temp._element, end = "-->")
            temp = temp._next
        print()
    
    def displayReverse(self):
        temp = self._tail
        while temp:
            print(temp._element, end="<--")
            temp = temp._prev
        print()

    def search(self, key):
        temp = self._head
        index = 0
        while temp:
            if temp._element == key:
                return index
            temp = temp._next
            index += 1
        return -1


dl = doublyLinkedList()
dl.addlast(10)
dl.addlast(20)
dl.addlast(30)
dl.displayForward()
dl.addfirst(40)
dl.addfirst(50)
dl.displayForward()
dl.addany(100, 3)
dl.displayForward()
print(dl.search(50))
dl.displayForward()
dl.displayForward()
print(dl.__len__())
dl.displayForward()
dl.displayReverse()
dl.removefirst()
dl.displayForward()