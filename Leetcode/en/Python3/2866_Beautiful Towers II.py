# @algorithm @lc id=3113 lang=python3 
# @title beautiful-towers-ii


from en.Python3.mod.preImport import *
# @test([5,3,4,1,1])=13
# @test([6,5,3,9,2,7])=22
# @test([3,2,5,5,2,3])=18
class Solution:
    """
        Prefix / Suffix + Monotonic Stack
        Monotonic Stack，Stack 中的元素值是單調遞增的
    """
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)

        # 前綴部分
        pre = [0] * (n + 1)
        st = [-1] # dummy, 用於計算區間長度
        s = 0
        for i, x in enumerate(maxHeights):
            while len(st) > 1 and x <= maxHeights[st[-1]]:
                j = st.pop()
                s -= maxHeights[j] * (j - st[-1]) # 這段區間的高度不能為 maxHeights[j] 了，所以要撤銷
            s += x * (i - st[-1]) # 這段區間的高度都是 x
            pre[i] = s
            st.append(i)

        # 後綴部分
        suf = [0] * (n + 1)
        st = [n] # dummy, 用於計算區間長度
        s = 0
        for i in range(n - 1, -1, -1):
            x = maxHeights[i]
            while len(st) > 1 and x <= maxHeights[st[-1]]:
                j = st.pop()
                s -= maxHeights[j] * (st[-1] - j) # 這段區間的高度不能為 maxHeights[j] 了，所以要撤銷
            s += x * (st[-1] - i) # 這段區間的高度都是 x
            suf[i] = s
            st.append(i)

        # 結果
        ans = suf[0]
        for i in range(n):
            ans = max(ans, pre[i] + suf[i + 1])
        return ans