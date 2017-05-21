from __future__ import print_function

class Heap(object):
    """
    Basic Heap structure (assume it's Max-Heap)
    """
    def __init__(self, heap_list=None):
        if heap_list is None:
            self.heap_list = [-1]
            self.size = 0
        else:
            self.heap_list = [-1] + heap_list[:]
            self.size = len(heap_list)

    def parent(self, index):
        """
        Return parent index location
        """
        return index / 2

    def left_child(self, index):
        """
        Return left child index location for current node
        """
        return 2 * index

    def right_child(self, index):
        """
        Return right child index location for current node
        """
        return 2 * index + 1

    def delete_max(self):
        """
        Delete maximum value from Max-Hep (which is at root node)
        """
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size = self.size - 1
        pop_val = self.heap_list.pop()
        self.percolate_down(1)
        return retval

    def insert(self, node_val):
        self.heap_list.append(node_val)
        self.size = self.size + 1
        self.percolate_up(self.size)

    def percolate_down(self, i):
        """
        Find the maximum of its children and swap it with the current element
        and continue this process until the heap property is satisfied at
        every node
        """
        while (i * 2) <= self.size:
            max_child = self.max_child(i)
            if self.heap_list[max_child] > self.heap_list[i]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[max_child]
                self.heap_list[max_child] = tmp
            i = max_child

    def max_child(self, i):
        """
        Return max child
        """
        if i * 2 >= self.size: # this parent only has one child
            return i * 2
        else:
            if self.heap_list[2 * i] < self.heap_list[2 * i + 1]:
                return 2 * i + 1
            else:
                return 2 * i


    def percolate_up(self, i):
        """
        Heapify the heap from bottom to up
        """
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def build_heap(self, arr):
        """
        Build a heap from list of length n

        start percolate_down from the first non-leaf nodes
        """
        i = len(arr) // 2
        self.size = len(arr)
        self.heap_list = [-1] + arr[:]
        while i > 0:
            self.percolate_down(i)
            i = i - 1
