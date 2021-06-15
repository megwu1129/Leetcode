class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return 
        
        dummy = Node(None)
        pred = [dummy]
        
        def dfs(node):
            if node.left is not None:
                dfs(node.left)
            
            
            pred[0].right = node
            node.left = pred[0]
            pred[0] = node
            
            if node.right is not None:
                dfs(node.right)
        dfs(root)
        pred[0].right = dummy.right
        dummy.right.left = pred[0]
        return dummy.right
        
