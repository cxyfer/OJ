from itertools import pairwise

def solve():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    A = [0] + A + [x + (x - A[-1])]
    print(max((b - a for a, b in pairwise(A))))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()