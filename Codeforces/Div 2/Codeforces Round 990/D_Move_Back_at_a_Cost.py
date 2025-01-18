"""
最後結果一定滿足單調非遞減，且操作會使字典序變大，因此應盡可能減少操作次數

先從 A 中找單調非遞減序列 q1 ，並將會破壞單調性的元素加入 q2 中。
由於操作順序可以影響插入順序，因此可以對 q2 進行排序，再將 q2 的元素插入 q1 中。
接著考慮 q2 的元素插入 q1 中，若插入會破壞 q1 單調性質，則將 q1 中會破壞單調性的元素重新放入 q2 中。
放入 q2 時，由於要維護 q2 單調非遞減性質，因此需要用 bisect 插入。
"""
from bisect import insort

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    q1 = [] # 在原陣列中找單調非遞減序列
    q2 = [] # 保存需要操作的元素
    for i, x in enumerate(A):
        while q1 and x < q1[-1]: # 破壞 q1 單調性質
            q2.append(q1.pop() + 1) # 將需要操作的元素加入 q2
        q1.append(x)

    q2.sort() # 從這裡開始也維護 q2 單調非遞減性質
    while q2:
        # 考慮將 q2 的隊首元素插入 q1 中
        while q1 and q2[0] < q1[-1]: # 破壞 q1 單調性質
            insort(q2, q1.pop() + 1) # 用 bisect 插入，維護 q2 單調性質
        q1.append(q2.pop(0))

    print(*q1)