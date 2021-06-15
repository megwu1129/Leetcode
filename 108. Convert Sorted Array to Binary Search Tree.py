class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(arr, start, end):
            if start > end:
                return None
            if start == end:
                return TreeNode(arr[start])
            
            mid = (start + end)//2
            root = TreeNode(arr[mid])
            
            root.left = helper(arr, start, mid-1)
            root.right = helper(arr, mid+1, end)
            
            return root
        return helper(nums, 0, len(nums)-1)
