import unittest

from src.lab3 import BinaryTree, post_order_traversal


class TestPostOrderTraversal(unittest.TestCase):
    def test_post_order_traversal(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        expected_result = [5, 2, 6, 7, 3, 1]

        result = post_order_traversal(root)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
