#iteration

    def inorderTraversal(self, root: TreeNode) -> List[int]:  
        result = []
        stack = []
        curr = root
        while len(stack) !=0 or curr is not None:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

#iteration - opt
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root is not None:
                stack.append(root)
                root = root.left
            if len(stack)==0:
                return res
            root = stack.pop()
            res.append(root.val)
            root = root.right
            
#recursion
    def inorderTraversal(self, root: TreeNode) -> List[int]:        
        result = []
        def helper(root):
            if root is not None:
                helper(root.left)
                result.append(root.val)
                helper(root.right)
            
        helper(root)
        return result
