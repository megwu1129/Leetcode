# recursion
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        
        def helper(root):
            if root is None:
                return 
            result.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return result
    
#iteration
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        stack = [root]
        while len(stack) != 0:
            node = stack.pop()
            result.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return result
