"""
CF2175A - Little Fairy's Painting
https://codeforces.com/problemset/problem/2175/A
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert n == len(A)

    A.sort()
    m = len(set(A))
    for x in A:
        if x >= m:
            print(x)
            return
    print(-1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()