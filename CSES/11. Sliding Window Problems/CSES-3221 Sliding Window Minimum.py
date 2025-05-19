from collections import deque

n, k = map(int, input().split())
x, a, b, c = map(int, input().split())

ans = s = 0
q = deque()
for i in range(n):
    # 1. 入窗口
    while q and q[-1][1] >= x:
        q.pop()
    q.append((i, x))

    # 2. 出窗口
    while q and q[0][0] <= i - k:
        q.popleft()

    # 3. 更新答案
    if i >= k - 1:
        ans ^= q[0][1]
    
    # 4. 更新生成器
    x = (a * x + b) % c

print(ans)