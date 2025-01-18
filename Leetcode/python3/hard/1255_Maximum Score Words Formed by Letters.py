#
# @lc app=leetcode id=1255 lang=python3
# @lcpr version=30202
#
# [1255] Maximum Score Words Formed by Letters
#



# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        return self.solve1(words, letters, score)
        # return self.solve2(words, letters, score)
    def solve1(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        cnt = Counter(letters) # 每個字母可使用的次數
        scores = {chr(i + 97): score[i] for i in range(26)} # 每個字母的分數
        ans, cur = 0, 0
        def dfs(i: int) -> None:
            nonlocal ans, cur
            if i == n:
                ans = max(ans, cur) # 更新答案
                return
            dfs(i + 1) # 不選 words[i]
            # 先減去 words[i] 的字母數量，若不能選 words[i] 則直接恢復，若能選則是遞迴後恢復
            for ch in words[i]:
                cnt[ch] -= 1
                cur += scores[ch]
            if all(cnt[ch] >= 0 for ch in cnt): # 判斷是否可以選 words[i]
                dfs(i + 1) # 選 words[i]
            for ch in words[i]:
                cnt[ch] += 1
                cur -= scores[ch]
        dfs(0)
        return ans
    def solve2(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        cnt = Counter(letters) # 每個字母可使用的次數
        scores = {chr(i + 97): score[i] for i in range(26)} # 每個字母的分數
        ans = 0
        for i in range(1, 1 << n): # 枚舉所有可能的子集
            tmp = Counter() # 當前子集需要的字母數量
            cur = 0 # 當前子集的分數
            for j in range(n):
                if i & (1 << j): # words[j] 在當前子集中
                    for ch in words[j]:
                        tmp[ch] += 1
                        cur += scores[ch]
                    if any(tmp[ch] > cnt[ch] for ch in tmp): # 這個子集不合法。這樣寫是為了不用 flag 變數
                        break
            else: # 若所有 words[j] 都能選，則更新答案
                ans = max(ans, cur)
        return ans
# @lc code=end

sol = Solution()
print(sol.maxScoreWords(["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))

#
# @lcpr case=start
# ["dog","cat","dad","good"]\n["a","a","c","d","d","d","g","o","o"]\n[1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]\n
# @lcpr case=end

# @lcpr case=start
# ["xxxz","ax","bx","cx"]\n["z","a","b","c","x","x","x"]\n[4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]\n
# @lcpr case=end

# @lcpr case=start
# ["leetcode"]\n["l","e","t","c","o","d"]\n[0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]\n
# @lcpr case=end

#

