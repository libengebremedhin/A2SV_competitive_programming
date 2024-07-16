class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        table, res = {}, []
        for c in p:
            table[c] = table.get(c, 0) + 1
        l, r = 0, len(p) - 1
        table2 = {}
        for d in s[:r]:
            table2[d] = table2.get(d, 0) + 1

        while r < len(s):
            table2[s[r]] = table2.get(s[r], 0) + 1

            if table2 == table:
                res.append(l)
            table2[s[l]] -= 1
            if table2.get(s[l], 0) < 1: del table2[s[l]]
            l += 1
            r += 1
        return res
                

