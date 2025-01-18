#
# @lc app=leetcode id=3143 lang=python3
# @lcpr version=30201
#
# [3143] Maximum Points Inside the Square
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start

class Solution:
    """
        1. Binary Search
        賽時寫了個很醜的對答案二分
        2. Counter
        但其實不用那麼麻煩，只要用 Counter 紀錄目前範圍內的標籤數量即可
        3. Set + Bitmask
    """
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        # return self.solve1(points, s)
        # return self.solve2(points, s)
        return self.solve3(points, s)
    """
        1. Binary Search
    """
    def solve1(self, points: List[List[int]], s: str) -> int:
        pos = defaultdict(list)
        for tag, (x, y) in zip(s, points):
            pos[tag].append(max(abs(x), abs(y)))
        for tag in pos:
            pos[tag].sort()

        def check(k): # 檢查是否有兩個同樣標籤的點在距離 k 內
            for tag in pos:
                if len(pos[tag]) <= 1:
                    continue
                idx = bisect_right(pos[tag], k)
                if idx >= 2:
                    return True
            return False
        left, right = 0, int(1e9)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        # print(right)
        ans = 0
        for tag in pos:
            if pos[tag][0] <= right:
                ans += 1
        return ans
    def solve2(self, points: List[List[int]], s: str) -> int:
        pos = defaultdict(Counter)
        for tag, (x, y) in zip(s, points):
            pos[max(abs(x), abs(y))][tag] += 1
        cnt = Counter() # 目前範圍內的標籤數量
        for k in sorted(pos.keys()):
            cnt += pos[k]
            if any(cnt[tag] >= 2 for tag in cnt):
                cnt -= pos[k]
                break
        return sum(cnt.values())
    def solve3(self, points: List[List[int]], s: str) -> int:
        mask = defaultdict(int) # set of tags
        for t, (x, y) in zip(s, points):
            d = max(abs(x), abs(y)) # distance
            c = ord(t) - ord('a')
            if mask[d] & (1 << c): # already exists
                mask[d] |= 1 << 26 # mark as invalid
            else: 
                mask[d] |= 1 << c # add tag
        union = 1 << 26
        for d, st in sorted(mask.items()): # sort by distance, from small to large
            if st & union: # invalid
                break
            union |= st
        return union.bit_count() - 1
# @lc code=end

sol = Solution()
print(sol.maxPointsInsideSquare([[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], "abdca")) # 2
print(sol.maxPointsInsideSquare([[1,1],[-2,-2],[-2,2]], "abb")) # 1
print(sol.maxPointsInsideSquare([[1,1],[-1,-1],[2,-2]], "ccd")) # 0
print(sol.maxPointsInsideSquare([[-1,-4],[16,-8],[13,-3],[-12,0]], "abda")) # 1


#
# @lcpr case=start
# [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]]\n"abdca"\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[-2,-2],[-2,2]]\n"abb"\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[-1,-1],[2,-2]]\n"ccd"\n
# @lcpr case=end

#

