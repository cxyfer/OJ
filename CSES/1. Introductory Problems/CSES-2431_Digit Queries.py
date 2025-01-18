""" CSES-2431 Digit Queries
    預處理長度為 x (x位數) 的數字總共佔據幾個字元，
    並以此求出目標是第幾個幾位數的第幾個字元。
"""
N = 20
cnt = [0] * N
cur = 1
for i in range(1, N): # i 位數
    cnt[i] = 9 * cur * i
    cur *= 10

t = int(input())

for _ in range(t):
    q = int(input())
    for i in range(1, N):
        if q <= cnt[i]:
            break
        q -= cnt[i]
    q -= 1 # i 位數的第 q 個字元 (0-indexed)
    x, y = divmod(q, i) # i 位數的第 x 個數字的第 y 個字元 (0-indexed)
    ans = 10 ** (i-1) + x
    print(str(ans)[y])
