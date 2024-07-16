class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, mySet = 0, set()
        res = 0
        for r in range(len(s)):
            while s[r] in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.add(s[r])
            res = max(res, r - l + 1)
        return res
                




        
