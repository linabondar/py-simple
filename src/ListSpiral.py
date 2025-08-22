import sys


def main():
    n = int(input())
    el = 0
    bound = n * n
    k = 0
    res = [[0 for j in range(n)] for i in range(n)]
    while el < bound:
        for j in range(k, n):
            res[k][j] = el + j - k + 1

        el = el + n - k
        if el >= bound:
            break

        for i in range(k, n):
            res[i][n - 1] = el + i - k
        el = el + n - 1 - k
        for j in range(n - 1, k - 1, -1):
            res[n - 1][j] = el + n - 1 - j
        el = el + n - 1 - k
        for i in range(n - 1, k, -1):
            res[i][k] = el + n - 1 - i
        el = el + n - 1 - (k + 1)

        n = n - 1
        k = k + 1

    # output result in required format
    for i in range(0, len(res)):
        print(" ".join(str(k) for k in res[i]))


if __name__ == "__main__":
    main()
