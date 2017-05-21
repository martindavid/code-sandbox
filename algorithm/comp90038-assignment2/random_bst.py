from __future__ import print_function


class RandomBSTNode(object):

    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.parent = None
        self.left = None
        self.right = None

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
        root = node
    else:
        if root.key > node.key:
            if root.get_left() is None:
                root.set_left(node)
                node.set_parent(root)
            else:
                insert_node(root.get_left(), node)
        else:
            if root.get_right() is None:
                root.set_right(node)
                node.set_parent(root)
            else:
                insert_node(root.get_right(), node)
    percolate_up(node)


def percolate_up(node):
    while node.parent is not None and node.parent.priority > node.priority:
        print("Check Node (%s:%d)" % (node.key, node.priority))
        # print("Check Node Parent (%s:%d)" %
        #       (node.parent.key, node.parent.priority))
        parent = node.parent
        if parent.parent is not None:
            node.parent = parent.parent
        else:
            node.parent = None
        parent.parent = node
        if node.key > parent.key:  # prev parent will become node left child
            if node.left is None:
                if is_leaf(node):
                    parent.left = None
                    parent.right = None
                node.left = parent
            else:
                if node.left.key > parent.key:
                    parent.right = node.left
                else:
                    parent.left = node.left
                node.left = parent
        else:  # prev parent will become node right child
            if node.right is None:
                if is_leaf(node):
                    parent.right = None
                    parent.left = None
                node.right = parent
            else:
                if node.right.key > parent.key:
                    parent.right = node.right
                else:
                    parent.left = node.right
                node.right = parent
        print_with_child(node)


def is_leaf(node):
    if node is None:
        return False
    return node.left is None and node.right is None


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
    #root_node = RandomBSTNode("G", 3)
    root_node = RandomBSTNode("F", 2)
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

    #child_f2 = RandomBSTNode("F", 2)
    child_m3 = RandomBSTNode("M", 3)
    insert_node(root_node, child_m3)

    print("")
    print_with_child(child_m3)
    print_with_child(child_b6)
    print_with_child(root_node)
    print_with_child(child_d9)
    print_with_child(child_k8)
    print_with_child(child_e14)
