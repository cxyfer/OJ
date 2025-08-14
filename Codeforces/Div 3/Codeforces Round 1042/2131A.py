"""
所求為操作 1 的能夠次數 + 1
"""
t = int(input())

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = sum(max(x - y, 0) for x, y in zip(A, B)) + 1
    print(ans)

for _ in range(t):
    solve()