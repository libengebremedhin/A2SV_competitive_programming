class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l, r = 0, 0
        res = ""
        while l < len(s) and r < len(spaces):
            if l == spaces[r]:
                res += " "
                r += 1
            else:
                res += s[l]
                l += 1
        res += s[l:]
        return res
            
        
