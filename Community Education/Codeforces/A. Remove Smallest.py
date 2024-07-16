for _ in range(int(input())):
    n = int(input())
    val = True
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(1, n):
        if abs(arr[i] - arr[i-1]) > 1:
            print("NO")
            val = False
            break
    if val:    
        print("YES")
