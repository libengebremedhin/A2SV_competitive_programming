class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        arr = [i for i in range(int(c ** 0.5) + 1)]
        l, r = 0, len(arr) - 1
       
        while l <= r:
            mid = (l + (r - l)) // 2
            if (arr[l] ** 2) + (arr[r] ** 2) > c:
                r -= 1
            elif (arr[l] ** 2) + (arr[r] ** 2) < c:
                l += 1
            elif (arr[l] ** 2) + (arr[l] ** 2) == c:
                return True
            elif (arr[r] ** 2) + (arr[r] ** 2) == c:
                return True
            else:
                return True   
        print(arr)
        return False
