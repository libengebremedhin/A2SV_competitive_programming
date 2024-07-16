class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        table = {}
        cnt = 0
        for n in nums:
            if (k-n) in table:
                cnt += 1
                if table[k-n] <= 1:
                    del table[k-n]
                else:
                    table[k-n] -= 1
            else:
                table[n] = table.get(n, 0) + 1
        return cnt
        
