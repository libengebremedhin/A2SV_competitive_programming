class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win, los, = [], []
        winners, losers = {}, {}
        for i, j in matches:
            winners[i] = winners.get(i, 0) + 1
            losers[j] = losers.get(j, 0) + 1
        for i, j in matches:
            if i not in losers:
                win.append(i)
            if losers.get(i, 0) == 1:
                los.append(i)
            if losers.get(j, 0) == 1:
                los.append(j)
        return [sorted(set(win)), sorted(set(los))]


        
