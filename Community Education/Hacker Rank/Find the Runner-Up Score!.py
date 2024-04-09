if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrSet = set(arr)
    newArr = sorted(list(arrSet))
    print(newArr[len(newArr)-2])
