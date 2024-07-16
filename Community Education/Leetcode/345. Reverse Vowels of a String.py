class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        myString = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        while r > l:
            if s[l].lower() in vowels and s[r].lower() in vowels:
                myString[l], myString[r] = myString[r], myString[l]
                l += 1
                r -= 1
            elif s[l].lower() in vowels:
                r -= 1
            elif s[r].lower() in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        return "".join(myString)
        
        
