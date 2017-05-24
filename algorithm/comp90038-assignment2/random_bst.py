from __future__ import print_function


class RandomBSTNode(object):

    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.parent = None
        self.left = None
        self.right = None
        self.is_root = False

    def set_left(self, node):
        self.left = node

    def get_left(self):
        return self.left

    def set_right(self, node):
        self.right = node

    def get_right(self):
        return self.right

    def set_parent(self, root):
        self.parent = root

    def get_parent(self):
        return self.parent


def insert_node(root, node):
    if root is None:
        parent = node
    else:
        if root.key > node.key:
            if root.get_left() is None:
                root.set_left(node)
                node.set_parent(parent)
            else:
                insert_node(root.get_left(), node)
        else:
            if root.get_right() is None:
                root.set_right(node)
                node.set_parent(parent)
            else:
                insert_node(root.get_right(), node)
    percolate_up(node)


def rotate_left(node):
    w = node.right
    w.parent = node.parent
    if w.parent is not None:
        if w.parent.left is node:
            w.parent.left = w
        else:
            w.parent.right = w
    node.right = w.left
    if node.right is not None:
        node.right.parent = node
    node.parent = w
    w.left = node
    if node.is_root:
        w.is_root = True
        node.is_root = False
        w.parent = None


def rotate_right(node):
    w = node.left # fetch node that we're going to restore the min-heap property
    w.parent = node.parent # 
    if w.parent is not None:
        if w.parent.left is node:
            w.parent.left = w
        else:
            w.parent.right = w
    node.left = w.right
    if node.left is not None:
        node.left.parent = node
    node.parent = w
    w.right = node
    if node.is_root:
        w.is_root = True
        w.parent = None
        node.is_root = False


def percolate_up(node):
    while node.parent is not None and node.parent.priority > node.priority:
        if node.parent.right is node:
            print("Left rotate foPr node %s:%d" % (node.parent.key, node.parent.priority))
            rotate_left(node.parent)
        else:
            print("Right rotate for node %s:%d" % (node.parent.key, node.parent.priority))
            rotate_right(node.parent)
    if node.parent is None:
        node.is_root = True

def print_with_parent(node):
    print("Parent for node (%s:%d) is (%s:%d)" %
          (node.key, node.priority, node.parent.key, node.parent.priority))


def print_with_child(node):
    left_key, left_priority = ("empty", 0) if node.get_left() is None else (
        node.get_left().key, node.get_left().priority)
    right_key, right_priority = ("empty", 0) if node.get_right() is None else (
        node.get_right().key, node.get_right().priority)
    print("Node (%s:%d) - left child: (%s:%d), right child: (%s:%d)" %
          (node.key, node.priority, left_key, left_priority, right_key, right_priority))

if __name__ == "__main__":
    root_node = RandomBSTNode("G", 3)
    root_node.is_root = True
    #root_node = RandomBSTNode("F", 2)
    child_b6 = RandomBSTNode("B", 6)
    child_k8 = RandomBSTNode("K", 8)
    child_a11 = RandomBSTNode("A", 11)
    child_e14 = RandomBSTNode("E", 14)
    child_l12 = RandomBSTNode("L", 12)

    root_node.set_left(child_b6)
    child_b6.set_parent(root_node)
    root_node.set_right(child_k8)
    child_k8.set_parent(root_node)

    child_b6.set_left(child_a11)
    child_a11.set_parent(child_b6)
    child_b6.set_right(child_e14)
    child_e14.set_parent(child_b6)
    child_k8.set_right(child_l12)
    child_l12.set_parent(child_k8)

    child_c16 = RandomBSTNode("C", 16)
    insert_node(root_node, child_c16)

    # print(child_e14.get_left().key)
    # print(child_e14.get_left().priority)
    # print("ChildC16 parent: %s:%d" %
    #       (child_c16.get_parent().key, child_c16.get_parent().priority))

    child_d9 = RandomBSTNode("D", 9)
    insert_node(root_node, child_d9)

    # print_with_parent(child_c16)
    # print_with_parent(child_e14)
    # print_with_parent(child_d9)
    # print_with_child(child_d9)

    child_f2 = RandomBSTNode("F", 2)
    insert_node(root_node, child_f2)
    #child_m3 = RandomBSTNode("M", 3)
    #insert_node(root_node, child_m3)

    print("")
    print_with_child(child_f2)
    print_with_child(child_b6)
    print_with_child(root_node)
    print_with_child(child_d9)
    print_with_child(child_k8)
    print_with_child(child_e14)
