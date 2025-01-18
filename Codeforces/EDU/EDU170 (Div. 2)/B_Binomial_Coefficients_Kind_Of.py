T = int(input())
MOD = 10**9 + 7

N = list(map(int, input().split()))
K = list(map(int, input().split()))

mx = max(K)
pow2 = [1] * (mx + 1)
for i in range(1, mx + 1):
    pow2[i] = (pow2[i-1] * 2) % MOD

for k in K:
    print(pow2[k])