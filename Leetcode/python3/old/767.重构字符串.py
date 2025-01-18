7#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#

# @lc code=start
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        idx = 0
        bucketNum = cnt.most_common(1)[0][1] # most_common(k) 取出頻率最高的k個元素，返回的是[(element, number)]，所以要取[0][1]
        buckets = [[] for _ in range(bucketNum)] # 用bucketNum個桶來存放element
        for c, num in cnt.most_common(): # most_common()返回的是所有n個 [(element, number)]
            for _ in range(num):
                buckets[idx].append(c)
                idx = (idx + 1) % bucketNum # 填入不同idx的bucket中，循環填入
        # 如果有兩個以上的桶只有一個元素，則無法構成答案
        if list(map(len, buckets)).count(1) > 1: 
            return ""
        else:
            return "".join(["".join(bucket) for bucket in buckets]) 
# @lc code=end
if __name__ == '__main__':
    sol = Solution()
    print(sol.reorganizeString("aab")) # "aba"
    print(sol.reorganizeString("aaab")) # ""

