if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    cors = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
    res = [[i, j, k] for [i,j,k] in cors if i + j + k != n]
    print(res)
