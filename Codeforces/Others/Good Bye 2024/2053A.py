from itertools import pairwise

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    for x, y in pairwise(A):
        if 2 * min(x, y) > max(x, y):
            print("YES")
            break
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()