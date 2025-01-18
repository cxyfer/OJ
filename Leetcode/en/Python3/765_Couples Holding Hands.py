# @algorithm @lc id=770 lang=python3 
# @title couples-holding-hands


from en.Python3.mod.preImport import *
# @test([0,2,1,3])=1
# @test([3,2,0,1])=0
class Solution:
    """
        Disjoint Set
        如果有 k 對情侶形成了錯誤環，需要交換 k - 1 次才能讓情侶牽手。
    """
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        fa = [i for i in range(n)]

        def find(x):
            if x != fa[x]:
                fa[x] = find(fa[x])
            return fa[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                fa[x] = y

        # 把相鄰位置的人 union 起來，若兩人不是同一對，則會形成cycle
        for i in range(0, n, 2):
            union(row[i]//2, row[i+1]//2)

        # n // 2 對情侶中，需要交換的情侶數量
        ans = 0
        for i in range(n//2):
            if i != find(i):
                ans += 1
        return ans
