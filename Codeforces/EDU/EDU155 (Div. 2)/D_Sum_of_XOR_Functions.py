# 思路來自：https://www.cnblogs.com/Zeoy-kkk/p/17738331.html

MOD = 998244353

N = int(input())
A = list(map(int, input().split(" ")))

ans = 0
 
for i in range(31):
    res = 0
    pre = [0] * (N+1)
    cnt = [0, 0]
    sss = [0, 0]
    cnt[0] += 1 # pre[0] = 0
    for j in range(N):
        pre[j+1] = pre[j] ^ (A[j] >> i & 1)
        cnt[pre[j+1]] += 1
        sss[pre[j+1]] += j+1
        res = (res + cnt[pre[j+1] ^ 1] * (j+1) - sss[pre[j+1] ^ 1]) % MOD
    ans = (ans + (1 << i) * res) % MOD
print(ans)