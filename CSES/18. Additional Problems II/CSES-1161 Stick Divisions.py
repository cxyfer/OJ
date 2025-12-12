"""
CSES-1161 Stick Divisions
https://cses.fi/problemset/task/1161

Huffman Coding
"""
from heapq import heapify, heappop, heappush

def solve():
    k, n = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n and sum(A) == k

    ans = 0
    heapify(A)
    while len(A) > 1:
        x, y = heappop(A), heappop(A)
        ans += x + y
        heappush(A, x + y)
    print(ans)

if __name__ == "__main__":
    solve()