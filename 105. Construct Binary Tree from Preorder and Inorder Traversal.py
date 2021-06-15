class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        dict1 = {}
        for i in range(len(inorder)):
            dict1[inorder[i]] = i
        def helper(P, startP, endP, I, startI, endI):
            if startP>endP:
                return None
            rootnode = TreeNode(P[startP])
            rootindex = dict1[P[startP]]
            numleft = rootindex - startI
            
            rootnode.left = helper(P, startP+1, startP+numleft, I, startI, rootindex-1)
            rootnode.right = helper(P, startP+1+numleft, endP, I, rootindex+1, endI)
            
            return rootnode
    
        return helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
