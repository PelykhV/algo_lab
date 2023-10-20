from typing import List


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right


def post_order_traversal(root: BinaryTree) -> List:
    if root is None:
        return []

    result = []

    if root.left is not None:
        result.extend(post_order_traversal(root.left))

    if root.right is not None:
        result.extend(post_order_traversal(root.right))

    result.append(root.value)

    return result


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

result = post_order_traversal(root)
print(result)
