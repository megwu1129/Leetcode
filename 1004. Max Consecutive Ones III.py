class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        longest = 0
        for j in range(len(nums)):
            if nums[j] != 1:
                k-=1
            while k < 0:
                if nums[i] == 0:
                    k+=1
                i+=1
            longest = max(longest, j-i+1)
        return longest
