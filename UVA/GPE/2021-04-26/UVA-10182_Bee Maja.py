"""
    注意到 N <= 10^5，所以先模擬出所有位置即可。
"""

N = int(1e5 + 5)
DIR = [(-1, 0), (0, -1), (1, -1), (1, 0), (0, 1)]
ans = [(-1, -1)] * N
i, k = 1, 0
while i < N:  
    ans[i] = (0, k)
    
    for m in range(k):  
        ans[i - m] = (m, k - m)
    
    cur = i
    x, y = ans[i]
    for dx, dy in DIR:
        for _ in range(k):
            x += dx
            y += dy
            cur += 1
            ans[cur] = (x, y)

    i += (6 * k) + 1
    k += 1

while True:
    try:
        n = int(input()) 
    except EOFError:
        break
    print(*ans[n])