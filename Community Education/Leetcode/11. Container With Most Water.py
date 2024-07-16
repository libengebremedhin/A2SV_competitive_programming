class Solution:
    def maxArea(self, height: List[int]) -> int:
        amount = []
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] > height[r]:
                amount.append((r - l) * height[r])
                r -= 1
            else:
                amount.append((r - l) * height[l])
                l += 1
            
        return max(amount)

        
