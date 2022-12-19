class _Node:
    __slots__ = '_element','_next'
    def __init__(self,element,next):
        self._element = element
        self._next = next

class singlyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    #find length of list
    def __len__(self):
        return self._size

    #check list is empty or not
    def isEmpty(self):
        return self._size == 0

    #add node at last
    def addLast(self,val):
        newNode = _Node(val,None)
        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
        else:
            self._tail._next = newNode
            self._tail = newNode
        self._size += 1

    #add node at begging
    def addFirst(self,val):
        newNode  = _Node(val,None)
        temp = self._head
        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
        else:
            newNode._next = temp
            self._head = newNode
            
        self._size +=1 

    #add node at anypoint
    def addAtAnyPoint(self,pos,val):
        newNode = _Node(val,None)
        temp = self._head
        if pos<=0:
            self.addFirst(val)
        elif pos >= self.__len__():
            self.addLast(e)
        else:
            i = 1
            while i < pos:
                temp = temp._next
                i = i+1
            newNode._next = temp._next
            temp._next = newNode
            self._size += 1
    
    #remove node at last
    def removeAtLast(self):
        r = None
        if self.isEmpty():
            print("List is empty")
        else:
            temp = self._head
            i = 1
            while i < self.__len__()-1:
                temp = temp._next
                i +=1 
            r = self._tail._element
            self._tail = temp
            self._tail._next = None
        self._size -= 1
        return r
            
    #Remove node at begining
    def removeAtBeg(self):
        if self.isEmpty():
            print("list is empty")
        else:
            temp = self._head
            self._head = temp._next
        self._size -= 1 
    
    #remove node at any point
    def removeAtAny(self,pos):
        if pos< 0 or pos >= self.__len__():
            print("List index out of range!")
        elif pos == 0:
            self.removeAtBeg()
        elif pos == self.__len__()-1:
            self.removeAtLast()
        else:
            temp = self._head
            i = 1
            while i < pos:
                temp = temp._next
                i = i+1
            temp._next = temp._next._next
            self._size -= 1

    #display the linkedlist
    def display(self):
        temp = self._head
        while temp:
            print(temp._element, end = "-->")
            temp = temp._next
        print()
    
    #search the elemnt in linkedlist
    def search(self,key):
        temp = self._head
        i = 0
        while i < self.__len__():
            if temp._element == key:
                return i
            temp = temp._next
            i +=1
        return -1
    

    

s1 = singlyLinkedList()
s1.addFirst(10)
s1.display()
s1.addLast(20)
s1.addLast(30)
s1.display()
s1.addFirst(40)
s1.display()
s1.removeAtLast()
s1.display()
s1.removeAtBeg()
s1.display()
s1.addLast(20)
s1.addLast(30)
s1.removeAtAny(3)
s1.display()
print(s1.search(10))