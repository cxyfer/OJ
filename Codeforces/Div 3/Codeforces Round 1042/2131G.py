MOD = int(1e9 + 7)
MAX_X = 32

# f[x] 表示完全移除 x 所需的操作次數
f = [0] * (MAX_X + 1)
for i in range(1, MAX_X + 1):
    f[i] = 1
    for j in range(1, i):
        f[i] += f[j]
    # assert f[i] == 1 << (i - 1)

# g[x] 表示完全移除 x 所能獲得的收益
g = [0] * (MAX_X + 1)
for i in range(1, MAX_X + 1):
    g[i] = i
    for j in range(1, i):
        g[i] = g[i] * g[j] % MOD

t = int(input())

def solve():
    n, k = map(int, input().split())
    S = list(map(int, input().split()))
    S.sort()

    # 剩下 k 次操作，移除 s 所能獲得的收益
    def helper(s, k):
        if k == 0:
            return 1
        # 移除 s 後，會出現 {1, 2, ..., s - 1} 這些數字，檢查是否能移除這些數字
        ans = s
        k -= 1  # 移除 s 本身算一次操作
        for x in range(1, s):
            if x <= MAX_X and k >= f[x]:  # 若 x 可以被完全移除，則完全移除 x
                k -= f[x]
                ans = ans * g[x] % MOD
            else:  # 若 x 不能被完全移除，則遞迴計算移除 x 的收益
                ans = ans * helper(x, k) % MOD
                break
        return ans

    ans = 1
    for x in S:
        if x <= MAX_X and k >= f[x]:
            k -= f[x]
            ans = ans * g[x] % MOD
        else:
            ans = ans * helper(x, k) % MOD
            break
    print(ans)

for _ in range(t):
    solve()