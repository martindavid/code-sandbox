# Binary Search Tree
class BSTNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data):
        """Set value for the current node"""
        self.data = data

    def get_data(self):
        """Return node value"""
        return self.data

    def get_left(self):
        """Get left child"""
        return self.left

    def get_right(self):
        """Get right child"""
        return self.right

    def find(self, root, data):
        """Find a node in the BST"""
        current_node = root
        while current_node is not None and current_node.get_data() != data:
            if data > current_node.get_data():
                current_node = current_node.get_right()
            else:
                current_node = current_node.get_left()
        return current_node

    def insert_node(self, root, node):
        """Insert new node into BST"""
        if root is None:
            root = node
        else:
            if root.data > node.data:
                if root.left is None:
                    root.left = node
                else:
                    self.insert_node(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    self.insert_node(root.right, node)

