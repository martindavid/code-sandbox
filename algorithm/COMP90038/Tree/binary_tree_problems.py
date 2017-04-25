from __future__ import print_function
import sys
sys.path.insert(0, 'Queue/')
from Queue import Queue
from binary_tree import BinaryTreeNode


def find_max_binary_tree(root):
    global max_data
    if not root:
        return max_data

    if root.get_data() > max_data:
        print('Check :' + str(root.get_data()))
        print('Max: ' + str(max_data))
        max_data = root.get_data()

    find_max_binary_tree(root.get_left())
    find_max_binary_tree(root.get_right())
    return max_data

def find_max_binary_tree_iterative(root):
    if not root:
        return

    q = Queue()
    q.en_queue(root)
    max_data = 0
    while not q.is_empty():
        node = q.de_queue()
        if (node.get_data() > max_data):
            max_data = node.get_data()
        if (node.get_left()):
            q.en_queue(node.get_left())
        if (node.get_right()):
            q.en_queue(node.get_right())
    return max_data


if __name__ == '__main__':
    root = BinaryTreeNode(1)
    max_data = 0
    root.insert_left(2)
    root.insert_right(3)
    root.get_left().insert_left(4)
    root.get_left().insert_right(5)
    root.get_right().insert_left(6)
    root.get_right().insert_right(7)

    # print("Final result")
    # print(find_max_binary_tree(root))

    find_max_binary_tree_iterative(root)
