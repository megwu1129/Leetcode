class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        result = [0]
        
        def dfs(node):
            if node.left is None and node.right is None:
                result[0] +=1
                return True
            
            amIuniValue = True
            
            if node.left is not None:
                is_left_unival = dfs(node.left)
                if not is_left_unival or node.val != node.left.val:
                    amIuniValue = False
            if node.right is not None:
                is_right_unival = dfs(node.right)
                if not is_right_unival or node.val != node.right.val:
                    amIuniValue = False
            
            if amIuniValue:
                result[0] += 1
            return amIuniValue
        
        dfs(root)
        return result[0]
