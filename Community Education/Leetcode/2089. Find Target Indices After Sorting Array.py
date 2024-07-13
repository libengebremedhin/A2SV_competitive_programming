class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        num = sorted(nums)
        for i, n in enumerate(num):
            if n == target:
                res.append(i)
        return res
