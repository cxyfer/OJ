from collections import defaultdict

N = int(input())
S = input().split()
L = [len(s) for s in S]
Sum = [ sum([int(S[i][j]) for j in range(L[i])]) for i in range(N) ]

# # pre[i][j] = k 表示 前i個數的和為j的個數為k
# pre = defaultdict(lambda: defaultdict(int))
# suf = defaultdict(lambda: defaultdict(int))

# for s in S:
#     n = len(s)
#     ss = 0
#     for i in range(n):
#         ss += int(s[i])
#         pre[i+1][ss] += 1
#     ss = 0
#     for i in range(n-1, -1, -1):
#         ss += int(s[i])
#         suf[n-i][ss] += 1
# print(pre)
ans = 0
for i in range(N):
    for j in range(N):
        if i == j:
            ans += 1
            continue
        if (L[i] + L[j]) % 2 != 0: # 長度為奇數
            continue
        if (L[i] == L[j]):
            if (Sum[i] == Sum[j]):
                ans += 1
        elif (L[i] > L[j]): # 長接短
            d = (L[i] - L[j]) // 2
            ti, tj = Sum[i], Sum[j]
            for k in range(L[i]-1, L[i]-1-d, -1):
                ti -= int(S[i][k])
                tj += int(S[i][k])
            if ti == tj:
                ans += 1
        else: # 短接長
            d = (L[j] - L[i]) // 2
            ti, tj = Sum[i], Sum[j]
            for k in range(d):
                ti += int(S[j][k])
                tj -= int(S[j][k])
            if ti == tj:
                ans += 1
print(ans)
            
