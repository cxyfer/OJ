#
# @lc app=leetcode id=857 lang=python3
# @lcpr version=30201
#
# [857] Minimum Cost to Hire K Workers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        令 r = wage / quality，那麼選定一個 r0 ，每個工人的實際薪水就是 r0 * quality。
        而對 ri <= r0 的工人，他們的實際薪水就會比預期的最低薪水高，這裡可以靠舉例來理解。
        因此我們可以對所有工人按照 r 值進行排序，對於前 k 名工人，選定 rk 就能滿足他們的薪水要求。

        由於實際的薪水只跟選定的 r0 和 quality 有關，所以我們可以統計選定工人的 quality 總和 sum_q，並維護一個Max Heap，保存所有選定工人的 quality。
        在遇到一個新的工人時，雖然 ri 會比 r0 大，但是 quality 可能會比堆頂的 quality 小，這樣就可以更新堆頂 和 sum_q ，得到更優的答案。

        Reference:
         - https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/solutions/1815856/yi-bu-bu-ti-shi-ru-he-si-kao-ci-ti-by-en-1p00/
    """
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = sorted(zip(quality, wage), key=lambda p: p[1] / p[0])  # 按照 r 值排序
        hp = [-q for q, _ in pairs[:k]] # Max Heap，保存選定的 k 名工人的 quality
        heapify(hp)
        sum_q = -sum(hp) # 選定的 k 名工人的 quality 總和
        ans = sum_q * pairs[k - 1][1] / pairs[k - 1][0] # 初始化答案為前 k 名工人的薪水總和，選擇 r0 = rk
        for q, w in pairs[k:]: # 遍歷剩下的工人，雖然 ri > r0，但是 quality 可能比堆頂的 quality 小
            if q < -hp[0]: # 如果 quality 比堆頂小
                sum_q += heapreplace(hp, -q) + q # 更新堆頂和 sum_q
                ans = min(ans, sum_q * w / q) # 更新答案
        return ans
# @lc code=end



#
# @lcpr case=start
# [10,20,5]\n[70,50,30]\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,1,10,10,1]\n[4,8,2,2,7]\n3\n
# @lcpr case=end

#

