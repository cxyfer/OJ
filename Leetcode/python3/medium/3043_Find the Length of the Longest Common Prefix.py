#
# @lc app=leetcode id=3043 lang=python3
# @lcpr version=30204
#
# [3043] Find the Length of the Longest Common Prefix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class TrieNode:
    def __init__(self):
        self.child = [None] * 10
        self.depth = 0
        
class Solution1:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def num_to_list(x):
            # return map(int, list(str(x)))
            res = []
            while x > 0:
                res.append(x % 10)
                x //= 10
            return res[::-1]

        root = TrieNode()
        for x in arr1:
            node = root
            for d in num_to_list(x):
                if node.child[d] is None:
                    node.child[d] = TrieNode() # type: ignore
                    node.child[d].depth = node.depth + 1
                node = node.child[d]

        ans = 0
        for x in arr2:
            node = root
            for d in num_to_list(x):
                if node.child[d] is None:
                    break
                node = node.child[d]
                ans = max(ans, node.depth)
        return ans

class Solution2:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        st = set()
        for x in arr1:
            while x > 0:
                st.add(x)
                x //= 10
        ans = 0
        for x in arr2:
            while x > 0:
                if x in st:
                    ans = max(ans, len(str(x)))
                    break
                x //= 10
        return ans

# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.longestCommonPrefix([1,10,100], [1000])) # 3
print(sol.longestCommonPrefix([1,2,3], [4,4,4])) # 0

#
# @lcpr case=start
# [1,10,100]\n[1000]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n[4,4,4]\n
# @lcpr case=end

#

