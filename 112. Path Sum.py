class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        
        result = [False]
        def dfs(node, target):
            if node.left is None and node.right is None:
                if node.val == target:
                    result[0] = True
                    return
            if node.left is not None:
                dfs(node.left, target-node.val)
            if node.right is not None:
                dfs(node.right, target-node.val)
        dfs(root, targetSum)
        return result[0]
