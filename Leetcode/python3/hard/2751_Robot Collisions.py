#
# @lc app=leetcode id=2751 lang=python3
# @lcpr version=30204
#
# [2751] Robot Collisions
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = sorted(zip(range(n), positions, healths, directions), key = lambda x: x[1])
        
        st = [] # 保存向右移動的機器人
        left = [] # 保存向左移動，且已經不會再發生碰撞的機器人
        for i, _, h, d in robots:
            if d == 'R': # 向右的機器人
                st.append([i, h])
            else: # 向左的機器人
                while st and st[-1][1] < h: # 把前面向右的機器人碰撞掉
                    h -= 1
                    st.pop()
                if st: # 還有向右的機器人，當前的會被碰撞掉
                    if st[-1][1] == h:
                        st.pop()
                    else: # st[-1][1] > h
                        st[-1][1] -= 1
                else:
                    left.append([i, h])
        left += st
        left.sort(key = lambda x: x[0])
        return [h for _, h in left]
# @lc code=end



#
# @lcpr case=start
# [5,4,3,2,1]\n[2,17,9,15,10]\n"RRRRR"\n
# @lcpr case=end

# @lcpr case=start
# [3,5,2,6]\n[10,10,15,12]\n"RLRL"\n
# @lcpr case=end

# @lcpr case=start
# [1,2,5,6]\n[10,10,11,11]\n"RLRL"\n
# @lcpr case=end

#

