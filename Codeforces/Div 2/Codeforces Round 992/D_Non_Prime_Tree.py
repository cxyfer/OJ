from collections import deque
 
t = int(input())
for _ in range(t):
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    ans = [0] * n

    # 相同奇偶性的數，相差是 2 的倍數，故除了相鄰兩數差 2 是質數以外，差值都不是質數
    st_e = set(range(2, 2 * n + 1, 2))
    st_o = set(range(3, 2 * n + 1, 2))
    dq_e = deque(range(2, 2 * n + 1, 2))
    dq_o = deque(range(3, 2 * n + 1, 2))
 
    q = deque([0])
    ans[0] = 1
    while q:
        u = q.popleft()
        first = True
        for v in g[u]:
            if ans[v] != 0:
                continue
            # 第 1 個 v 可以嘗試選 ans[u] + 1 來轉換奇偶性
            if (ans[u] + 1) in st_e or (ans[u] + 1) in st_o:
                ans[v] = ans[u] + 1
                st_e.discard(ans[v])
                st_o.discard(ans[v])
            # 第 2 個以後的 v 選相同奇偶性的數，相差是 2 的倍數，除了 2 以外都不是質數
            else:
                if ans[u] & 1:
                    while dq_o and dq_o[0] not in st_o:
                        dq_o.popleft()
                    while dq_o and dq_o[-1] not in st_o:
                        dq_o.pop()
                    ans[v] = dq_o.pop() if abs(dq_o[0] - ans[u]) == 2 else dq_o.popleft()
                    st_o.discard(ans[v])
                else:
                    while dq_e and dq_e[0] not in st_e:
                        dq_e.popleft()
                    while dq_e and dq_e[-1] not in st_e:
                        dq_e.pop()
                    ans[v] = dq_e.pop() if abs(dq_e[0] - ans[u]) == 2 else dq_e.popleft() 
                    st_e.discard(ans[v])
            q.append(v)
    print(*ans)