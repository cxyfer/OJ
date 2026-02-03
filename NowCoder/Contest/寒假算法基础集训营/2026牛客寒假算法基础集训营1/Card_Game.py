"""
B. Card Game
https://ac.nowcoder.com/acm/contest/120561/B

當 A[i] < min(B) 時，A[i] 以及 A 中之後的數字都不可能被刪除
因此最優策略是將 A 中所有 > min(B) 的數字放在前面，使其能夠被 min(B) 刪除
因此答案為 cnt! * (n - cnt)!，其中 cnt 為 A 中 > min(B) 的數字個數
"""
MOD = 998244353
MAX_N = int(2e5 + 5)
fact = [1] * MAX_N
for i in range(2, MAX_N):
    fact[i] = (fact[i-1] * i) % MOD

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    min_b = min(B)
    cnt = sum(1 for x in A if x > min_b)
    ans = (fact[cnt] * fact[n - cnt]) % MOD
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()