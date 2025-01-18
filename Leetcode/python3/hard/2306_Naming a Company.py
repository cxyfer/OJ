#
# @lc app=leetcode id=2306 lang=python3
# @lcpr version=30204
#
# [2306] Naming a Company
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. 按照首字母分組
    2. 按照後綴分組 -> C++ 會 TLE
    3. 按照後綴分組 + 預處理集合和交集大小
"""
class Solution1:
    """
        idea_i 和 idea_j 不能交換的情況：
        1. 首字母相同，交換後必在 ideas 中
            => 故可以按照首字母分組
        2. 首字母不同，且 idea_i 的首字母加上 idea_j 的後綴，組合後的字串在 ideas 中，也無法交換
            => 故需扣除兩個分組的交集
    """
    def distinctNames(self, ideas: List[str]) -> int:
        # 將每個 idea 根據首字母分組，並儲存其後綴
        groups = defaultdict(set)
        for idea in ideas:
            first, suffix = idea[0], idea[1:]
            groups[first].add(suffix)
        
        letters = list(groups.keys())
        n = len(letters)
        ans = 0
        # 枚舉所有可能的首字母組合
        for i in range(n):
            A = letters[i]
            for j in range(i+1, n):
                B = letters[j]
                intersection = len(groups[A] & groups[B]) # 交集
                unique_A = len(groups[A]) - intersection
                unique_B = len(groups[B]) - intersection
                ans += unique_A * unique_B * 2
        return ans
    
class Solution2:
    def distinctNames(self, ideas: List[str]) -> int:
        # 按照後綴分組，並儲存其首字母
        groups = defaultdict(set)
        for idea in ideas:
            first, suffix = idea[0], idea[1:]
            groups[suffix].add(first)

        ans = 0
        suffixes = list(groups.keys()) # 所有的後綴
        # 枚舉所有可能的首字母組合
        for i in range(26):
            A = chr(ord('a') + i)
            for j in range(i+1, 26):
                B = chr(ord('a') + j)

                suffix_A_not_B = 0 # 計算A首字母擁有但B首字母沒有的後綴數量
                suffix_B_not_A = 0 # 計算B首字母擁有但A首字母沒有的後綴數量
                for suffix in suffixes:
                    has_A = A in groups[suffix]
                    has_B = B in groups[suffix]
                    if has_A and not has_B:
                        suffix_A_not_B += 1
                    elif has_B and not has_A:
                        suffix_B_not_A += 1
                
                ans += suffix_A_not_B * suffix_B_not_A * 2
        return ans

class Solution3:
    def distinctNames(self, ideas: List[str]) -> int:
        sz = [0] * 26 # 集合的大小
        intersection = [[0] * 26 for _ in range(26)] # 交集的大小
        groups = defaultdict(list) # 後綴 -> 首字母
        for idea in ideas:
            first, suffix = idea[0], idea[1:]
            B = ord(first) - ord('a')
            sz[B] += 1
            for A in groups[suffix]:
                intersection[A][B] += 1
                intersection[B][A] += 1
            groups[suffix].append(B)
        
        ans = 0
        # 枚舉所有可能的首字母組合
        for i in range(26):
            for j in range(i+1, 26):
                m = intersection[i][j]
                ans += (sz[i] - m) * (sz[j] - m) * 2
        return ans
        
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.distinctNames(["coffee","donuts","time","toffee"])) # 6
print(sol.distinctNames(["lack","back"])) # 0

#
# @lcpr case=start
# ["coffee","donuts","time","toffee"]\n
# @lcpr case=end

# @lcpr case=start
# ["lack","back"]\n
# @lcpr case=end

#

