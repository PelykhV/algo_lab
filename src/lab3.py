class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def post_order_traversal(root: BinaryTree):
    if root is None:
        return []

    result = []

    if root.left is not None:
        result.extend(post_order_traversal(root.left))

    if root.right is not None:
        result.extend(post_order_traversal(root.right))

    result.append(root.value)

    return result
