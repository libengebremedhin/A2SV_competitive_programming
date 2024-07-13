class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        cnt = Counter(words[0])
        for w in words:
            cur_cnt = Counter(w)
            for k in cnt.keys():
                cnt[k] = min(cnt[k], cur_cnt[k])
        for c in cnt:
            for v in range(cnt[c]):
                res.append(c)
        return res
