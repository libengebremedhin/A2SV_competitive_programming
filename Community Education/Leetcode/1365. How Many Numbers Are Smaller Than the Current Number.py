class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        num  = sorted(nums)
        ans = []
        for n in nums:
            ans.append(num.index(n))
        return ans
        


        
