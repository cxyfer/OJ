from heapq import *

n = int(input())
A = list(map(int, input().split()))
B = sorted(A)

pre = [0] * n
suf = [0] * n
ans = n * n

#First pass: forward direction
hp1, hp2 = [], []
for i in range(n):
    heappush(hp1, A[i])
    heappush(hp2, B[i])
    while hp1 and hp2 and hp1[0] == hp2[0]:
        heappop(hp1)
        heappop(hp2)
    if not hp1: # 代表此時可以透過排序前 i + 1 個數字來使得前綴排序
        pre[i] = 1
    # 此時前綴有 i + 1 個數字需要排序，後綴有 n - (i + 1) 個數字需要排序
    # 但排序後又有 len(hp1) 個數字需要再和後綴排序，因此後綴排序的數字有 n - (i + 1) +  len(hp1) 個
    ans = min(ans, (i + 1) ** 2 + (n - (i + 1) + len(hp1)) ** 2)

# Clear queues
hp1.clear()
hp2.clear()

# Second pass: backward direction
for i in range(n - 1, -1, -1):
    heappush(hp1, -A[i])
    heappush(hp2, -B[i])
    while hp1 and hp2 and hp1[0] == hp2[0]:
        heappop(hp1)
        heappop(hp2)
    if not hp1: # 代表此時可以透過排序後 i + 1 個數字來使得後綴排序
        suf[i] = 1
    # 此時後綴有 n - i 個數字需要排序，前綴有 i 個數字需要排序
    # 但排序後又有 len(hp1) 個數字需要再和後綴排序，因此後綴排序的數字有 n - (i + 1) +  len(hp1) 個
    ans = min(ans, (n - i) ** 2 + (i + len(hp1)) ** 2)

nxt = n # 需要排序的後綴起始位置
for i in range(n - 1, -1, -1):
    if pre[i] == 1:
        ans = min(ans, (i + 1) * (i + 1) + (n - nxt) * (n - nxt))
    if A[i] != B[i]: # 需要重新確定後綴起始位置
        nxt = -1
    if suf[i] == 1: # 更新後綴起始位置
        nxt = max(nxt, i)

# 如果本來前綴或後綴已經是有序的，則只需要排序剩下的數字
for i in range(n):
    if A[i] != B[i]:
        break
    ans = min(ans, (n - (i + 1)) * (n - (i + 1)))
for i in range(n - 1, -1, -1):
    if A[i] != B[i]:
        break
    ans = min(ans, i * i)

print(ans)