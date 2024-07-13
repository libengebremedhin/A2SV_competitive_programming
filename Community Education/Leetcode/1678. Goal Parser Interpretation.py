class Solution:
    def interpret(self, com: str) -> str:
        res = ""
        c = 0
        while c < len(com):
            if com[c] == "G":
                res += "G"
                c += 1
            elif com[c+1] == ")":
                res += "o"
                c += 2
            else:
                res += "al" 
                c += 4
        return res 
