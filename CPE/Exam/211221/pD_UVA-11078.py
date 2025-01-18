"""
    Greedy
"""
import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

for _ in range(t):
    n = int(input())
    A = [int(input()) for _ in range(n)]
    ans = -float('inf')
    mx = A[0]
    for i in range(1, n):
        ans = max(ans, mx - A[i])
        mx = max(mx, A[i])
    print(f"{ans}\n")