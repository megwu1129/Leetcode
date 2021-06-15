class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        result = []
        
        def dfs(node, targetSum, path):
            path.append(node.val)
            if node.left is None and node.right is None:
                if node.val == targetSum:
                    result.append(path.copy())
                path.pop()
                return
            if node.left is not None:
                dfs(node.left, targetSum-node.val, path)
            if node.right is not None:
                dfs(node.right, targetSum-node.val, path)
            path.pop()
            
              
        dfs(root, targetSum, [])
        return result
