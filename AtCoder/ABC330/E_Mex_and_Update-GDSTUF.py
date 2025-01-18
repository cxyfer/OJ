from collections import Counter
from heapq import *

N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

cnt = Counter(A)
# min heap 維護沒有出現過的最小的數字
st = set(range(N))
for i in range(N):
    if cnt[i] > 0:
        st.remove(i)
hp = list(st)
heapify(hp)

for i, x in queries:
    i = i - 1
    cnt[A[i]] -= 1
    if cnt[A[i]] == 0 and A[i] < N: # 可能為答案，push 進 heap
        heappush(hp, A[i])
    cnt[x] += 1
    A[i] = x

    while hp:
        x = hp[0]
        if cnt[x] == 0: # 答案
            break
        else:
            heappop(hp) # 非答案，pop 掉
        x = N
    print(x)
