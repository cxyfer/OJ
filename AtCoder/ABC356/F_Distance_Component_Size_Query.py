"""
    縮點 + 有序集合

    s1 是所有點的集合、s2 會把一個連通塊的點縮成最大那個點 (縮點)
    需要對 s1 求 rank ，所以使用 SortedSet

    Reference:
     - https://atcoder.jp/contests/abc356/submissions/54141391
     - https://atcoder.jp/contests/abc356/submissions/54110078
"""
from sortedcontainers import SortedSet

Q, K = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]

# s1 是所有點的集合；s2 會把一個連通塊的點縮成最大那個點 (縮點)
s1, s2 = SortedSet([-10**19, 10**19]), SortedSet([-10**19, 10**19])

for op, x in queries:
    if op == 1:
        if x in s1: # 刪除操作
            i = s1.index(x)
            w1, w2 = s1[i - 1], s1[i + 1] # x 左右兩個點
            s1.remove(x)
            if x in s2:
                s2.remove(x)
            if (x - w1 <= K) and (w2 - w1 > K): # 讓 w1 重新出現在 s2 中
                s2.add(w1)
        else: #  插入操作
            s1.add(x)
            i = s1.index(x)
            w1, w2 = s1[i - 1], s1[i + 1] # x 左右兩個點
            if (x - w1 <= K) and (w2 - w1 > K): # 不需要 w1 ，且原本 w1 在 s2 中
                s2.remove(w1)
            if w2 - x > K: # 需要 x
                s2.add(x)
    else:
        idx = s2.bisect_left(x) # x 所屬連通塊中的最大值的索引
        pre, cur = s2[idx - 1], s2[idx] # 所屬連通塊中的最大值、前一個連通塊的最大值
        print(s1.index(cur) - s1.index(pre)) # 連通塊大小