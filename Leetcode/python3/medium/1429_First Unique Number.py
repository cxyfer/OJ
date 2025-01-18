#
# @lc app=leetcode id=1429 lang=python3
# @lcpr version=30204
#
# [1429] First Unique Number
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.cnt = defaultdict(int)
        for x in nums:
            self.cnt[x] += 1
        for x in nums:
            if self.cnt[x] == 1:
                self.q.append(x)

    def showFirstUnique(self) -> int:
        while self.q and self.cnt[self.q[0]] > 1:
            self.q.popleft()
        return self.q[0] if self.q else -1
        

    def add(self, value: int) -> None:
        self.cnt[value] += 1
        if self.cnt[value] == 1:
            self.q.append(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
# @lc code=end



#
# @lcpr case=start
# ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"][[[2,3,5]],[],[5],[],[2],[],[3],[]]\n
# @lcpr case=end

# @lcpr case=start
# ["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"][[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]\n
# @lcpr case=end

# @lcpr case=start
# ["FirstUnique","showFirstUnique","add","showFirstUnique"][[[809]],[],[809],[]]\n
# @lcpr case=end

#

