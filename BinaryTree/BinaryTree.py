class Root:
    __slots__ = '_element','_left','_right'
    def __init__(self,element,left,right):
        self._element = element
        self._left = left
        self._right = right


class BinaryTree:
    def __init__(self):
        self.root = None