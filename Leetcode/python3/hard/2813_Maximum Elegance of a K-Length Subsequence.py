#
# @lc app=leetcode id=2813 lang=python3
# @lcpr version=30203
#
# [2813] Maximum Elegance of a K-Length Subsequence
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        n = len(items)
        items.sort(key= lambda x : x[0], reverse=True)
        cur = 0
        seen = set() # 已經出現過的種類
        dulplicate = [] # 所有種類中，第二個以後的物品，利潤由大到小

        for i in range(min(k, n)): # 先加入前 k 個物品
            profit, category = items[i]
            cur += profit
            if category in seen: # 重複的種類
                dulplicate.append(profit)
            else: # 新的種類
                seen.add(category)

        ans = cur + len(seen) * len(seen) # 初始化答案為前 k 個物品的利潤 + 種類數量的平方
        for i in range(k, n):
            profit, category = items[i]
            # 有新的種類，且之前有重複種類的物品，則取代最小的重複物品，嘗試看看會不會讓答案變大
            if dulplicate and category not in seen:
                seen.add(category)
                cur += profit - dulplicate.pop() # 去除重複種類的物品中，利潤最小的
                ans = max(ans, cur + len(seen) * len(seen)) # 更新答案
        return ans
# @lc code=end

sol = Solution()
print(sol.findMaximumElegance([[3,2],[5,1],[10,1]], 2))
print(sol.findMaximumElegance([[3,1],[3,1],[2,2],[5,3]], 3))


#
# @lcpr case=start
# [[3,2],[5,1],[10,1]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[3,1],[3,1],[2,2],[5,3]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,1],[3,1]]\n3\n
# @lcpr case=end

#

