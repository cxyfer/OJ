from collections import deque

n, k = map(int, input().split())
x, a, b, c = map(int, input().split())

ans = s = 0
q = deque()
for i in range(n):
    # 1. 入窗口
    s += x
    q.append(x)
    # 2. 出窗口
    if i >= k:
        s -= q.popleft()
    # 3. 更新答案
    if i >= k - 1:
        ans ^= s
    # 4. 更新生成器
    x = (a * x + b) % c

print(ans)