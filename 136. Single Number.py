class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dict1 = {}
        for num in nums:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1
        for ele in dict1:
            if dict1[ele] == 1:
                return ele
