"""
    前綴和 + 雜湊表 + 貪心

    由於我們要使美麗子陣列數量越多，因此每個子陣列應該要越短越好，
    因此我們維護 prefix sum 最後一次出現的位置，

    如果當前 prefix sum 曾經出現過，並且出現的位置在上一個美麗子陣列的後面，
    那麼我們就可以形成一個新的美麗子陣列。
"""

from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    ans = s = 0
    pos = defaultdict(int)
    pos[str(s)] = -1
    last = -1
    for i, x in enumerate(A):
        s += x
        if str(s) in pos:
            if pos[str(s)] >= last: # 不重疊
                ans += 1
                last = i
        pos[str(s)] = i
    print(ans)