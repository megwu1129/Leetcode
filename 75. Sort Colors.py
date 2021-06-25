class Solution:
    def sortColors(self, nums: List[int]) -> None:        
        red = 0
        white = 0
        blue = len(nums)-1
        
        while white <= blue:
            if nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue-=1
            elif nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red+=1
                white+=1
            else:
                white+=1
        return nums
    
    # count sort    
def sortColors1(self, nums):
    c0 = c1 = c2 = 0
    for num in nums:
        if num == 0:
            c0 += 1
        elif num == 1:
            c1 += 1
        else:
            c2 += 1
    nums[:c0] = [0] * c0
    nums[c0:c0+c1] = [1] * c1
    nums[c0+c1:] = [2] * c2
