class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def minValueNode(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


def deleteNode(root, key):

    if root is None:
        return root

    if key < root.data:
        root.left = deleteNode(root.left, key)

    elif key > root.data:
        root.right = deleteNode(root.right, key)

    else:

        # Node with one or no child
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        # Node with two children
        temp = minValueNode(root.right)

        root.data = temp.data

        root.right = deleteNode(root.right, temp.data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Driver Code
root = None

values = [50, 30, 20, 40, 70, 60, 80]

for i in values:
    root = insert(root, i)

print("Inorder before deletion:")
inorder(root)

key = int(input("\nEnter value to delete: "))

root = deleteNode(root, key)

print("Inorder after deletion:")
inorder(root)