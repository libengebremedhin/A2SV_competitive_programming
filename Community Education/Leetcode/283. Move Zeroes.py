class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for n in range(len(nums)):
            if nums[n]:
                nums[i], nums[n] = nums[n], nums[i]
                i += 1

            
        
        
