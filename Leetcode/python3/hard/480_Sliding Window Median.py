#
# @lc app=leetcode id=480 lang=python3
# @lcpr version=30201
#
# [480] Sliding Window Median
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
from sortedcontainers import SortedList

class Solution:
    """
        Two Heaps + Sliding Window
        Similar to 295. Find Median from Data Stream
    """
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # return self.solve1(nums, k)
        # return self.solve2(nums, k)
        return self.solve3(nums, k)
    """
        1. Binary Search
        Time: O(nk)
    """
    def solve1(self, nums: List[int], k: int) -> List[float]:
        def get_median(arr):
            n = len(arr)
            return (arr[(n-1)//2] + arr[n//2]) / 2
        cur = sorted(nums[:k]) # window
        ans = [get_median(cur)]
        for _in, _out in zip(nums[k:], nums[:-k]):
            cur.remove(_out)
            bisect.insort(cur, _in)
            ans.append(get_median(cur))
        return ans
    """
        2. SortedList
        Time: O(nlogk)
    """
    def solve2(self, nums: List[int], k: int) -> List[float]:
        def get_median(arr):
            n = len(arr)
            return (arr[(n-1)//2] + arr[n//2]) / 2
        cur= SortedList(nums[:k])
        ans = [get_median(cur)]
        for _in, _out in zip(nums[k:], nums[:-k]):
            cur.remove(_out)
            cur.add(_in)
            ans.append(get_median(cur))
        return ans
    """
        3. Two Heaps + Hash Table + Lazy Deletion
        Extended from 295. Find Median from Data Stream
        由於窗口大小固定為 k ，因此可以使用 Lazy Deletion 來實現刪除操作
        但這樣會讓我們不能單純用左右兩個堆的大小來判斷插入時的位置，
        不過在窗口大小固定後，左右兩邊的實際大小就固定了，可以從被刪除的數字的所在的位置來判斷插入的位置。
        Time: O(nlogk)
    """
    def solve3(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        l = [] # max heap，保存 <= median 的數字
        r = [] # min heap，保存 > median 的數字
        cnt = Counter() # Lazy deletion，保存要刪除的數字及其應該刪除的次數
        
        def get_median():
            # Lazy deletion，若堆頂的數字已經被標記為刪除，則刪除
            while l and cnt[-l[0]] > 0: # 注意這裡取出的是 -l[0]，因為 l 是 max heap
                cnt[-l[0]] -= 1
                heappop(l)
            while r and cnt[r[0]] > 0:
                cnt[r[0]] -= 1
                heappop(r)
            return -l[0] if k & 1 else (-l[0] + r[0]) / 2.0 # 窗口大小固定為 k ，以其奇偶性來判斷中位數
        
        def insert(num, toLeft): 
            if toLeft:
                heappush(l, -heappushpop(r, num))
            else:
                heappush(r, -heappushpop(l, -num))
            
        for i in range(k): # 初始化窗口
            if len(l) == len(r): # 當前數量為偶數，加入到左邊
                insert(nums[i], True)
            else: # 當前數量為奇數，加入到右邊
                insert(nums[i], False)
        ans = [get_median()]
        for _in, out in zip(nums[k:], nums[:-k]):
            cnt[out] += 1 # 出窗口，標記為刪除
            insert(_in, True if out <= -l[0] else False) # 根據被刪除的數字在左邊還是右邊，插入新的數字
            ans.append(get_median())
        return ans
# @lc code=end
sol = Solution()
print(sol.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # [1, -1, -1, 3, 5, 6]
print(sol.medianSlidingWindow([1,2,3,4,2,3,1,4,2], 3)) # [2, 3, 3, 3, 2, 3, 2]

#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,2,3,1,4,2]\n3\n
# @lcpr case=end

#

