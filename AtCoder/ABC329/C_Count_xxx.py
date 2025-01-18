from collections import *

N = int(input())
S = input()


cnt = defaultdict(int)
tmp = S[0]
cnt[S[0]] = 1
for i in range(1, N):
    if S[i-1] == S[i]:
        tmp += S[i]
    else:
        cnt[S[i-1]] = max(cnt[S[i-1]], len(tmp)) 
        tmp = S[i]
cnt[tmp[0]] = max(cnt[tmp[0]], len(tmp)) 
ans = 0
for k, v in cnt.items():
    ans += v
print(ans)
