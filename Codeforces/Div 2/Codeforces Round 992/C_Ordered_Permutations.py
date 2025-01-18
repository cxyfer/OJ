# from collections import defaultdict
# from itertools import permutations

# N = 5
# res = defaultdict(list)
# for p in permutations(range(1, N + 1)):
#     cur = 0
#     for i in range(1, len(p) + 1):
#         for j in range(i):
#             cur += min(p[j:i])
#     res[cur].append(p)
# mx = max(res.keys())
# res[mx].sort()
# print(res[mx])

# 當前最小值要填在開頭或結尾，接著遞迴填入剩下的數字

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k > (1 << (n - 1)):
        print(-1)
        continue
    ans = [-1] * n
    st, ed = 0, n - 1
    cur = 1
    while cur < n:
        if k > (1 << (n - 1 - cur)):
            k -= (1 << (n - 1 - cur))
            ans[ed] = cur
            ed -= 1
        else:
            ans[st] = cur
            st += 1
        cur += 1
    ans[st] = n
    print(*ans)
        
