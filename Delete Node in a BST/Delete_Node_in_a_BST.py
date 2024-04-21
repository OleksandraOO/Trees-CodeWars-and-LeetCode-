class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        # base case for recursion
        if not root:
            return root

        # searching for a node we need to delete
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # found the node
        else:
            # if it has only one son - return him
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # searching for the smallest value in the right part of the tree to replace deleted node with it
            current = root.right
            while current.left:
                current = current.left
            root.val = current.val
            root.right = self.deleteNode(root.right, root.val)
        return root
