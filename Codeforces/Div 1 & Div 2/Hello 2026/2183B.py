def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    st = set(A)
    mex = 0
    while mex in st:
        mex += 1
    print(min(mex, k - 1))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()