from __future__ import print_function
from binary_tree import BinaryTreeNode

def preorderTraversal(root, result):
    if not root:
        return
    result.append(root.data)
    preorderTraversal(root.left, result)
    preorderTraversal(root.right, result)

def inorderTraversal(root, result):
    if not root:
        return

    inorderTraversal(root.left, result)
    result.append(root.data)
    inorderTraversal(root.right, result)

def postorderTraversal(root, result):
    if not root:
        return

    postorderTraversal(root.left, result)
    postorderTraversal(root.right, result)
    result.append(root.data)


if __name__ == '__main__':
    root = BinaryTreeNode(1)
    root.insert_left(2)
    root.insert_right(3)
    root.get_left().insert_left(4)
    root.get_left().insert_right(5)
    root.get_right().insert_left(6)
    root.get_right().insert_right(7)

    print('Preorder Traversal')
    preorder_result = []
    preorderTraversal(root, preorder_result)
    print(preorder_result)

    print('Inorder Traversal')
    inorder_result = []
    inorderTraversal(root, inorder_result)
    print(inorder_result)

    print('Postorder Traversal')
    postorder_result = []
    postorderTraversal(root, postorder_result)
    print(postorder_result)
