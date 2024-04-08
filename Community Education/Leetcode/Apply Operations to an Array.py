class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        r = 0
        res = [0] * len(nums)
        for l in range(len(nums)):
            if nums[l]:
                res[r] = nums[l]
                r += 1
        return res
