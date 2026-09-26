class Solution:
    def binaryTreePaths(self, root):
        result = []
        def find(node, path):
            if node is None:
                return
            path += str(node.val)
            if node.left is None and node.right is None:
                result.append(path)
                return
            path += "->"
            find(node.left, path)
            find(node.right, path)
        find(root, "")
        return result