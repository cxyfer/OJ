from bisect import bisect_left, bisect_right, insort
from sortedcontainers import SortedList

t = int(input())
for _ in range(t):
    n = int(input())
    users = []
    for _ in range(n):
        li, ri = map(int, input().split())
        users.append((li, ri))
    
    L = [-1] * n
    R = [-1] * n
    
    # 按l升序，r降序排序
    sorted_by_l = sorted(range(n), key=lambda i: (users[i][0], -users[i][1]))
    sorted_rs = SortedList()
    for j in range(n):
        i = sorted_by_l[j]
        l_i, r_i = users[i]
        idx_r = bisect_left(sorted_rs, r_i)
        if idx_r < len(sorted_rs):
            R[i] = sorted_rs[idx_r]
        else:
            R[i] = -1
        sorted_rs.add(r_i)
        if j + 1 < n and users[sorted_by_l[j]][0] == users[sorted_by_l[j + 1]][0] and users[sorted_by_l[j]][1] == users[sorted_by_l[j + 1]][1]:
            R[i] = users[i][1]
    
    # 按r降序，l升序排序
    sorted_by_r = sorted(range(n), key=lambda i: (-users[i][1], users[i][0]))
    sorted_ls = SortedList()
    for j in range(n):
        i = sorted_by_r[j]
        l_i, r_i = users[i]
        idx_l = bisect_right(sorted_ls, l_i)
        if idx_l > 0:
            L[i] = sorted_ls[idx_l - 1]
        else:
            L[i] = -1
        sorted_ls.add(l_i)
        if j + 1 < n and users[sorted_by_r[j]][1] == users[sorted_by_r[j + 1]][1] and users[sorted_by_r[j]][0] == users[sorted_by_r[j + 1]][0]:
            L[i] = users[i][0]
    
    # 計算並輸出每個用戶的強力推薦歌曲數量
    ans_list = []
    for i in range(n):
        if L[i] == -1:
            ans = 0
        else:
            ans = R[i] - L[i] - (users[i][1] - users[i][0])
            if ans < 0:
                ans = 0
        print(ans)