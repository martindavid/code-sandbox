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
    root = BinaryTreeNode('E')
    root.insert_left('C')
    root.insert_right('H')
    nodeC = root.get_left()
    nodeH = root.get_right()
    nodeC.insert_left('B')
    nodeC.insert_right('D')
    nodeC.get_left().insert_left('A')

    nodeH.insert_left('F')
    nodeH.insert_right('I')
    nodeH.get_left().insert_right('G')

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

    print("\nExample 2")
    root11 = BinaryTreeNode(11)
    root11.insert_left(4)
    root11.insert_right(10)
    
    node4 = root11.get_left()
    node4.insert_left(0)
    node4.insert_right(3)
    node4.get_right().insert_left(1)
    node4.get_right().insert_right(2)

    node10 = root11.get_right()
    node10.insert_left(6)
    node10.insert_right(9)
    node10.get_left().insert_left(5)
    node10.get_right().insert_left(7)
    node10.get_right().insert_right(8)

    print('Preorder Traversal')
    preorder_result = []
    preorderTraversal(root11, preorder_result)
    print(preorder_result)

    print('Inorder Traversal')
    inorder_result = []
    inorderTraversal(root11, inorder_result)
    print(inorder_result)

    print('Postorder Traversal')
    postorder_result = []
    postorderTraversal(root11, postorder_result)
    print(postorder_result)
