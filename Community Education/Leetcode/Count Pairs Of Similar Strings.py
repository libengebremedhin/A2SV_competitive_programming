class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        mySet = [set(word) for word in words]
        for w in range(len(words)):
            for k in range(w + 1, len(words)):
                if mySet[w] == mySet[k]:
                    res += 1
        return res
