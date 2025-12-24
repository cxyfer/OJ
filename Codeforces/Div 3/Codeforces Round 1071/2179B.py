from itertools import pairwise

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    s = sum(abs(x - y) for x, y in pairwise(A))
    mx = max(abs(A[1] - A[0]), abs(A[-1] - A[-2]))
    for i in range(1, n - 1):
        mx = max(mx, abs(A[i] - A[i - 1]) + abs(A[i + 1] - A[i]) - abs(A[i + 1] - A[i - 1]))
    print(s - mx)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()