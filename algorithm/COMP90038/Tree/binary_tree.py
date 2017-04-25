# Binary tree
class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    # get left child
    def get_left(self):
        return self.left

    # get right child
    def get_right(self):
        return self.right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinaryTreeNode(new_node)
        else:
            temp = BinaryTreeNode(new_node)
            temp.left = self.left
            self.left = temp

    def insert_right(self, new_node):
        if self.right is None:
            self.right = BinaryTreeNode(new_node)
        else:
            temp = BinaryTreeNode(new_node)
            temp.right = self.right
            self.right = temp
