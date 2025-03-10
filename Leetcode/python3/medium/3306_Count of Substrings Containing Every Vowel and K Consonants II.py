#
# @lc app=leetcode.cn id=3306 lang=python3
# @lcpr version=30204
#
# [3306] 元音辅音字符串计数 II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = set('aeiou')

        # pre[i] 表示 word[i] 前面有多少個連續的母音 (不含 word[i])
        pre = [0] * n
        for i in range(n - 1):
            if word[i] in vowels:
                pre[i + 1] = pre[i] + 1

        cnt_vowel = defaultdict(int)
        have_vowel = 0 # 母音的種類

        ans = 0
        cnt = 0 # 子音的數量
        left = 0
        for right, ch in enumerate(word):
            # 1. 入窗口
            if ch in vowels:
                if cnt_vowel[ch] == 0:
                    have_vowel += 1
                cnt_vowel[ch] += 1
            else:
                cnt += 1

            # 2. 子音太多了，縮小窗口
            while cnt > k:
                lc = word[left]
                if lc in vowels:
                    cnt_vowel[lc] -= 1
                    if cnt_vowel[lc] == 0:
                        have_vowel -= 1
                else:
                    cnt -= 1
                left += 1

            # 3. 更新答案
            if cnt == k and have_vowel == 5:
                # 把前綴中多餘的母音去掉
                while left < right and word[left] in vowels and cnt_vowel[word[left]] > 1:
                    cnt_vowel[word[left]] -= 1
                    left += 1
                # pre[left] 即窗口可以向左延伸的長度
                ans += pre[left] + 1

        return ans
# @lc code=end



#
# @lcpr case=start
# "aeioqq"\n1\n
# @lcpr case=end

# @lcpr case=start
# "aeiou"\n0\n
# @lcpr case=end

# @lcpr case=start
# "ieaouqqieaouqq"\n1\n
# @lcpr case=end

#

