# @algorithm @lc id=2165 lang=python3 
# @title plates-between-candles


from en.Python3.mod.preImport import *
# @test("**|**|***|",[[2,5],[5,9]])=[2,3]
# @test("***|**|*****|**||**|*",[[1,17],[4,5],[14,17],[5,11],[15,16]])=[9,0,0,0,0]
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        pre_sum = [0] * (n+1) # pre_sum[i+1] 表示前i個物品中的盤子數量
        l, r = [-1] * n, [-1] * n # l[i]/r[i] 表示第i個蠟燭 左邊/右邊 最近的盤子的位置 (包括自己)，若無則為-1
        for i in range(n):
            j = n-1-i
            l[i] = i if s[i] == '|' else (l[i-1] if i > 0 else -1)
            r[j] = j if s[j] == '|' else (r[j+1] if j < n-1 else -1)
            pre_sum[i+1] = pre_sum[i] + (s[i] == '*')
        # print(l, r, pre_sum, sep='\n')
        ans = [0] * len(queries)
        for i, (a, b) in enumerate(queries):
            c, d = r[a], l[b]
            if c != -1 and d != -1 and c <= d: # d != -1 is not necessary
                ans[i] = pre_sum[d] - pre_sum[c]
        return ans