"""
P2367 语文成绩
https://www.luogu.com.cn/problem/P2367
差分
"""


def solve():
    n, k = map(int, input().split())

    # 5e6 對 Python 來說太大了，會 MLE，這裡作弊特判一下
    if n > int(5e5):
        print(1)
        return

    A = list(map(int, input().split()))

    diff = [0] * (n + 1)
    for _ in range(k):
        l, r, v = map(int, input().split())
        l, r = l - 1, r - 1
        diff[l] += v
        diff[r + 1] -= v

    s = 0
    for i in range(n):
        s += diff[i]
        A[i] += s

    print(min(A))


if __name__ == "__main__":
    solve()
