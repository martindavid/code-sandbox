from __future__ import print_function
from PriorityQueue.heap import Heap
from PriorityQueue.heap_sort import HeapSort

if __name__ == "__main__":
    heap_array = [31, 1, 21, 9, 10, 12, 18, 3, 2, 8, 7]
    # heap = Heap(heap_array)
    # print(heap.heap_list)

    # print("Parent of %d is %d" %
    #       (heap.heap_list[9], heap.heap_list[heap.parent(9)]))

    # heap.percolate_down(2)
    # after_percolate = [node for node in heap.heap_list]
    # print(after_percolate)

    # heap.delete_max()
    # after_delete = [node for node in heap.heap_list]
    # print("After Delete Max: ", after_delete)

    # heap.insert(13)
    # after_insert = [node for node in heap.heap_list]
    # print("After insert 13: ", after_insert)

    # print("Build heap from a list")
    random_arr = [1, 5, 14, 2, 10, 21, 18, 3, 11, 8, 7, 12]
    sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print("Initial value: ", random_arr)
    # heap.build_heap(random_arr)
    # after_heapify = [node for node in heap.heap_list]
    # print("After heapify: ", after_heapify)

    # print("Perform HeapSort for random array")
    # heap_sort = HeapSort(random_arr)
    # heap_sort.sort()
    # after_sort = [node for node in heap_sort.heap_list]
    # print(after_sort)

    print("Perform heapsort for sorted array")
    print(sorted_arr)
    heap_sort = HeapSort(sorted_arr)
    heap_sort.sort()
    after_sort = [node for node in heap_sort.heap_list]
    print(after_sort)

    # print(heap_sort.sort_2(random_arr))
