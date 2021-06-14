class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        q = deque([root])
        
        while len(q) != 0:
            count = len(q)
            temp = []
            
            for _ in range(count):
                node = q.popleft()
                temp.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                    
            result.append(temp)
        return result
