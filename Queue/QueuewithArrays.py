class queueList:
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def isempty(self):
        return len(self) == 0

    def enqueue(self, val):
        self._queue.append(val)

    def dequeue(self):
        r = None
        if self.isempty():
            print("Queue is empty!...")
        else:
            r = self._queue.pop(0)

        return r

    def first(self):
        r = None
        if self.isempty():
            print("Queue is empty!...")
        else:
            r = self._queue[0]
        return r

    def display(self):
        for i in self._queue:
            print(i, end = "<--")
        print()

Qll = queueList()
Qll.enqueue(10)
Qll.enqueue(20)
Qll.enqueue(30)
Qll.enqueue(40)
Qll.enqueue(50)
Qll.display()
Qll.dequeue()
Qll.display()
