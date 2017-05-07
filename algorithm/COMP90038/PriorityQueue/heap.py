
class Heap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def parent(self, index):
        """
        Parent will be at index/2
        """
        return index/2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def get_maximum(self, index):
        """
        Assuming that this is a MAX-HEAP, so the maximum element
        will be at root
        """
        return self.heap_list[0]
    
    def percolate_down(self, i):
        while (i * 2) <= self.size:
            minimum_child = self.