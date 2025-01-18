"""
    Greedy + Queue
    先算所有的花費，再減去可以節省的部分

    倒序遍歷
    - 如果當前天數可以買，把可以買的日期放到 queue 中：
    - 如果當前天數不能買，則代表一定需要和後面的某天一起買，此時選擇最後可以買的日期，能節省最多花費。
    - 最後將佇列中剩下的天數兩兩配對，節省花費
"""
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = n * (n + 1) // 2 
    q = deque()
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            q.append(i + 1)
        else:
            if q:
                ans -= q.popleft()
    # 剩下的還能兩兩配對，則用較小的買買，節省的金額為較大的
    while len(q) > 1:
        ans -= q.popleft()
        q.pop()

    print(ans)