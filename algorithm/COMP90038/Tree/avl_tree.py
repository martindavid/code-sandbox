from __future__ import print_function

class AVLNode(object):
    def __init__(self, data, balance_factor, left, right):
        self.data = data
        self.balance_factor = balance_factor
        self.left = left
        self.right = right

class AVLTree(object):

    def __init__(self):
        self.root = None

    def in_order_print(self):
        self.rec_in_order_print(self.root)

    def rec_in_order_print(self, root):
        if root != None:
            self.rec_in_order_print(root.left)
            print(root.data)
            self.rec_in_order_print(root.right)

    def single_right_rotate(self, root):
        W = root.left
        root.left = W.right
        W.right = root
        return W

    def single_left_rotate(self, root):
        X = root.right
        root.right = X.left
        X.left = root

    def left_right_rotate(self, root):
        

    def height(self, root):
        return self.rec_height(root)

    def rec_height(self, root):
        if root == None:
            return 0
        else:
            left_height = self.rec_height(root.left)
            right_heigth = self.rec_height(root.right)
            if left_height > right_heigth:
                return 1 + left_height
            else:
                return 1 + right_heigth
