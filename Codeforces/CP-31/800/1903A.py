from itertools import pairwise

def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    print("YES" if all(a <= b for a, b in pairwise(A)) or k >= 2 else "NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()