from heapq import nsmallest

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    a, b = nsmallest(2, A)
    print(max(a, b - a))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()