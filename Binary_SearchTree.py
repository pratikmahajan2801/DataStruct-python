# Binary search tree implementation

class MyTreeNode:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

class MyBinarySearchTree:
    def __init__(self):
        self.root_node = None

    def insert_node(self, val):
        self.root_node = self._insert(self.root_node, val)

    def _insert(self, root, val):
        if root is None:
            return MyTreeNode(val)

        if val < root.val:
            root.left_child = self._insert(root.left_child, val)
        elif val > root.val:
            root.right_child = self._insert(root.right_child, val)

        return root

    def search_value(self, val):
        return self._search(self.root_node, val)

    def _search(self, root, val):
        if root is None or root.val == val:
            return root

        if val < root.val:
            return self._search(root.left_child, val)
        else:
            return self._search(root.right_child, val)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root_node, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left_child, result)
            result.append(root.val)
            self._inorder_traversal(root.right_child, result)

