#
# @lc app=leetcode.cn id=2182 lang=python3
#
# [2182] 构造限制重复的字符串
#
from preImport import *
# @lc code=start
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ans = []
        cnt = Counter(s)
        keys = sorted(cnt.keys(), reverse=True)
        n = len(keys)
        print(cnt)
        for i, k in enumerate(keys): # 由大到小
            if cnt[k] == 0:
                continue
            j = i + 1
            while True:
                if ans and ans[-1] == k: # 重複的字母，先pop出來加回去
                    ans.pop()
                    cnt[k] += 1
                num = min(cnt[k], repeatLimit) # 重複次數
                if num == 0:
                    break
                ans.append(k*num)
                cnt[k] -= num
                while j < n and cnt[keys[j]] == 0:
                    j += 1
                if j == n:
                    break
                ans.append(keys[j])
                cnt[keys[j]] -= 1
        return "".join(ans)
# @lc code=end
sol = Solution()
print(sol.repeatLimitedString("cczazcc",3)) # "zzcccac"
print(sol.repeatLimitedString("aababab",2)) # "bbabaa"
print(sol.repeatLimitedString("pdprlxqryxdirdr", 10)) # "yxxrrrrqppliddd"