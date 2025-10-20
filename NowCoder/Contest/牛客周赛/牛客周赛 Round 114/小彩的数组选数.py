"""
D-小彩的数组选数
https://ac.nowcoder.com/acm/contest/119273/D

雖然敘述方式不太一樣，但本質上就是經典的 198. House Robber
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))

    f = [0] * (n + 1)
    for i, x in enumerate(A, 1):
        if i >= 2:
            f[i] = max(f[i - 1], f[i - 2] + x)
        else:
            f[i] = x
    print(f[n])

if __name__ == "__main__":
    solve()