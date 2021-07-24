# set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for num in nums:
            if num not in set1:
                set1.add(num)
            else:
                return True
        return False

# sort
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
      
      
# set len
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      return len(set(nums)) != len(nums)
