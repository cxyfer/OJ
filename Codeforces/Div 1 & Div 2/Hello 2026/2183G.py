from bisect import bisect_left

def query(s: str):
    print(f"? {s}", flush=True)
    k, *arr = list(map(int, input().split()))
    assert k == len(arr)
    return arr

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    vl = query("L")
    vlr = query("LR")
    vr = query("R")
    assert len(vl) == len(vlr)

    k = len(vlr)
    ans = [-1] * n

    j = 0
    for i, x in enumerate(A):
        if j < k and vlr[j] == x:
            ans[i] = x - vl[j]
            j += 1

    for i in range(1, n):
        if ans[i] == -1:
            d = A[i] - A[i - 1]
            # if (d == 1 and ans[i - 1] == 1) or (d == 2 and ans[i - 1] == 0):
            if (d == 1 and ans[i - 1] != 0) or (d == 2 and ans[i - 1] == 0):
                ans[i] = 2

    for i, x in enumerate(A):
        if ans[i] == -1:
            j = bisect_left(vr, x)
            ans[i] = vr[j] - x

    for i in range(n - 2):
        if A[i + 1] - A[i] == A[i + 2] - A[i + 1] == 1:
            if ans[i] == 0 and ans[i + 1] != 0 and ans[i + 2] == 0:
                print("! -1", flush=True)
                return
    print("!", *ans, flush=True)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()