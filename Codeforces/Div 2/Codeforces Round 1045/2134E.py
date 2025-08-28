"""
2134E - Power Boxes
https://codeforces.com/contest/2134/problem/E
交互式、構造

令 f[i] 為 throw(i) 的結果，令 f[n + 1] = f[n + 2] = 0。
有一個比較容易觀察到的性質：
如果 f[i + 1] != f[i + 2]，則可以在詢問 f[i] 後得到轉移來源，進而確定 A[i] 的值；
否則 f[i] = f[i + 1] + 1 = f[i + 2] + 1，但無法確定 A[i] 的值。

那麼接下來就是把操作次數壓在 ceil(3n/2) 內。
如果 i 位置無法確定 A[i]，那麼 i-1 位置一定可以確定 A[i-1]，
因此「並不會連續出現」兩個無法使用前述方法確定 A[i] 的 i，故可以分別用1次操作確定至少一半的 A[i]。

接著考慮剩下的位置，根據前述結論，如果 i 位置無法確定 A[i]，那麼 i+1 位置一定可以確定 A[i+1]，
故交換 i 和 i+1 位置，並且確認 throw(i+1) 即可確定 A[i]。
注意 n 位置一定無法被確定，且不能往後換，因此 A[n] 需要交換 n-1 和 n 位置後由 throw(n-1) 確認。
"""
def swap(x):
    print(f"swap {x}", flush=True)

def throw(x):
    print(f"throw {x}", flush=True)
    return int(input().strip())

def solve():
    n = int(input())
    ans = ["!"] + [-1] * n
    f = [-1] * n + [1, 0, 0]

    # 從後往前計算 f[i]
    for i in range(n - 1, 0, -1):
        # 可以在詢問 f[i] 後確定 A[i]
        if f[i + 1] != f[i + 2]:
            f[i] = throw(i)
            if (f[i] == f[i + 1] + 1):
                ans[i] = 1
            else:
                ans[i] = 2
        # 不能確定 A[i]，但可以直接計算出 f[i]
        else:
            f[i] = f[i + 1] + 1
    # 從前往後確定 A[i]
    for i in range(1, n):
        if ans[i] != -1:
            continue
        swap(i)
        if throw(i + 1) == f[i + 2] + 1:
            ans[i] = 1
        else:
            ans[i] = 2
    # 最後確定 A[n]
    swap(n - 1)
    if throw(n - 1) == f[n] + 1:
        ans[n] = 1
    else:
        ans[n] = 2

    print(*ans, flush=True)
    return

t = int(input())
for _ in range(t):
    solve()