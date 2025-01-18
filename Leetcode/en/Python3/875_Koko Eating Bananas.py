# @algorithm @lc id=907 lang=python3 
# @title koko-eating-bananas


from en.Python3.mod.preImport import *
# @test([3,6,7,11],8)=4
# @test([30,11,23,4,20],5)=30
# @test([30,11,23,4,20],6)=23
class Solution:
    """
        Binary search
        對每小時吃的香蕉數 k 進行二分搜尋
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles): # 時間 h 剛好等於堆數 len(piles)
            return max(piles)
        left, right = 1, max(piles)

        def check(k): # 每小時吃 k 根香蕉，是否能在 h 小時內吃完所有香蕉
            s = 0
            for x in piles: 
                s += math.ceil(x / k)
            return s <= h
        
        while (left <= right):
            mid = (left + right) // 2
            if not check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left
