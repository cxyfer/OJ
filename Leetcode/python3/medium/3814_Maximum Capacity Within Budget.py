#
# @lc app=leetcode id=3814 lang=python3
#
# [3814] Maximum Capacity Within Budget
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
題意：選出 m1, m2 ，使得 m1.cost + m2.cost < budget 且 m1.capacity + m2.capacity 最大

1. 排序 + 二分 + 前綴最大值
不妨設 m1.cost <= m2.cost，並枚舉 m2 ，則可能的 m1 需滿足 m1.cost < budget - m2.cost
按照 cost 排序，可以讓 m1 的下標範圍落在一個區間內，可以二分出這個範圍的右端點
又由於區間是前綴的，可以維護前綴最大值來查找有最大 capacity 的 m1

2. 排序 + 雙指標 + 前綴最大值
類似 1.，但可以注意到當 m2.cost 增大時，可能的 m1 範圍會向左逐漸縮減，所以可以用雙指標來維護這個範圍
但注意需要限制區間的上界不能超過 i - 1

3. 排序 + 單調堆疊
考慮當區間縮減時，若原本的最大值被移出區間，會有甚麼變化？
此時最大值會變成前綴中的次大值，故可以用單調堆疊來維護
"""
# @lc code=start
class Solution1:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        machines = [(cost, cap) for cost, cap in zip(costs, capacity) if cost < budget]
        machines.sort()
        pre_mx = list(accumulate(machines, func=lambda mx, p: max(mx, p[1]), initial=0))
        ans = 0
        for i, (cost, cap) in enumerate(machines):
            # note: complexity of range() is O(1)
            j = bisect_left(range(i), budget - cost, key=lambda j: machines[j][0])
            # (j - 1) + 1 == j
            ans = max(ans, cap + pre_mx[j])
        return ans

class Solution2:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        machines = [(cost, cap) for cost, cap in zip(costs, capacity) if cost < budget]
        machines.sort()
        pre_mx = list(accumulate(machines, func=lambda mx, p: max(mx, p[1]), initial=0))
        ans = 0
        j = len(machines) - 1
        for i, (cost, cap) in enumerate(machines):
            while j >= 0 and machines[j][0] >= budget - cost:
                j -= 1
            # (j - 1) + 1 == j
            ans = max(ans, cap + pre_mx[min(i - 1, j) + 1])
        return ans

class Solution3:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        machines = [(cost, cap) for cost, cap in zip(costs, capacity) if cost < budget]
        machines.sort()
        ans = 0
        st = [(0, 0)]  # sentinel
        for cost, cap in machines:
            # pop out the maximum value if it is out of the budget
            while cost + st[-1][0] >= budget:
                st.pop()
            ans = max(ans, cap + st[-1][1])
            # maintain monotone increasing stack
            if cap > st[-1][1]:
                st.append((cost, cap))
        return ans

# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.maxCapacity([4,8,5,3], [1,5,2,7], 8))  # 8
print(sol.maxCapacity([3,5,7,4], [2,4,3,6], 7))  # 6
