class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        single = []
        double = []
        for p in people:
            if p >= limit:
                single.append(p)
            else:
                double.append(p)
        double.sort()
        l, r = 0, len(double) - 1
        res = len(single)
        while l <= r:
            if double[l] + double[r] > limit:
                res += 1
                r -= 1
            else:
                res += 1
                l += 1
                r -= 1
        return res

