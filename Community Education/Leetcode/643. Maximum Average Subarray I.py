class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        ans = float("-inf")
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            if r - l + 1 == k:
                ans = max(ans, total/k)
                total -= nums[l]
                l += 1
        return ans
        
