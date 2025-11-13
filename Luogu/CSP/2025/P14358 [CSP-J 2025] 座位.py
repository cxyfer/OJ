"""
P14358 [CSP-J 2025] 座位 / seat
https://www.luogu.com.cn/problem/P14358
"""
def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    
    x = A[0]
    A.sort(reverse=True)
    i = A.index(x)
    c, r = divmod(i, n)
    if c & 1:
        r = n - 1 - r
    print(c + 1, r + 1)

if __name__ == "__main__":
    solve()