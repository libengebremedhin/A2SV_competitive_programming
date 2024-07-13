class Solution:
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles)
        i , j = 0 , n - 2
        summ = 0
        while i < j:
            summ += piles[j]
            j -= 2
            i += 1
        return summ
