class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev, original = 0, x
        while x > 0:
            temp = x % 10
            x = x // 10
            rev = (rev * 10) + temp
        if original == rev:
            return True
        else:
            return False
