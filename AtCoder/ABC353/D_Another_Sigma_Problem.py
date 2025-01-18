"""
    考慮貢獻
    若一個數字在右邊，則該組貢獻是自己本身，總貢獻是其左邊的數字數量
    若一個數字在左邊，則該組貢獻與右邊的數字位數 d 有關，是 x * 10^d

    從右到左枚舉會比較好寫
"""
N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

cnt = [0] * 11 # 右邊每個位數數字的數量
ans = 0
for i in range(N-1, -1, -1):
    ans = (ans + A[i] * i) % MOD
    p = 10
    for j in range(1, 11):
        ans = (ans + A[i] * cnt[j] * p) % MOD
        p = p * 10
    cnt[len(str(A[i]))] += 1
print(ans)

