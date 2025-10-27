"""
B - 小L出师了
https://ac.nowcoder.com/acm/contest/95337/B

更簡潔的作法是直接算 min((n - k) // t, k + 1)
"""
def solve():
    n, t, k = map(int, input().split())

    x = min((n - k) // t, k)
    r = n - x * t - k  # 剩餘需要主講人講的場次
    print(x + 1 if r >= t else x)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()