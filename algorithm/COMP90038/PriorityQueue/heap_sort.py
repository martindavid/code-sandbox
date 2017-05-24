from __future__ import print_function
from heap import Heap

class HeapSort(object):

    def __init__(self, arr):
        self.heap_list = arr

    def sort(self):
        # Convert arr into heap
        length = len(self.heap_list) - 1
        least_parent = length / 2
        for i in range(least_parent, -1, -1):
            self.percolate_down(self.heap_list, i, length)

        # flatten heap into sorted array
        for i in range(length, 0, -1):
            if self.heap_list[0] > self.heap_list[i]:
                self.swap(self.heap_list, 0, i)
                #print("%d swap" % i)
                print(self.heap_list)
                self.percolate_down(self.heap_list, 0, i - 1)

    def sort_2(self, arr):
        heap = Heap()
        i = len(arr)
        heap.build_heap(arr)
        result = []
        while i > 0:
            result.append(heap.delete_max())
            i = i - 1
        return result


    def percolate_down(self, arr, first, last):
        """
        Modified percolate_down to skip the sorted elements
        """
        largest = 2 * first + 1
        while largest <= last:
            # right child exists and is larger than left child
            if (largest < last) and (arr[largest] < arr[largest + 1]):
                largest += 1

            # right child is larger than parent
            if arr[largest] > arr[first]:
                self.swap(arr, largest, first)
                # move down to largest child
                first = largest
                largest = 2 * first + 1
            else:
                return


    def swap(self, arr, x, y):
        temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp
