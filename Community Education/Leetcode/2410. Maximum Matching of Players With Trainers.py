class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p, t = 0, 0
        cnt = 0
        while p < len(players) and t < len(trainers):
            if trainers[t] >= players[p]:
                t += 1
                p += 1
                cnt += 1
            else:
                t += 1
        return cnt

        
