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
