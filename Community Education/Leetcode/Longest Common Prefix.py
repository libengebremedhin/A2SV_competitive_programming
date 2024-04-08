class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in range(1, len(strs)):
            for c in range(len(res)):
                if c == len(strs[s]) or strs[s][c] != res[c]:
                    res = res[:c]
                    break
        return res

        
