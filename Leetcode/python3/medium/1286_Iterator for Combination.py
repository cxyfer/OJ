#
# @lc app=leetcode id=1286 lang=python3
# @lcpr version=30204
#
# [1286] Iterator for Combination
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.k = combinationLength
        self.s = list(characters)
        self.comb = list(range(self.k))
        self.has_next = True

    def next(self) -> str:
        ans = "".join([self.s[p] for p in self.comb])
        for i in range(self.k - 1, -1, -1):
            if self.comb[i] != self.n - self.k + i:  # 此時最後的 x 個元素不是最大的 x 個元素
                self.comb[i] += 1
                for j in range(i + 1, self.k):
                    self.comb[j] = self.comb[j - 1] + 1
                # assert self.comb[self.k - 1] == self.comb[i] + (self.k - i - 1)
                break
        else:
            self.has_next = False
        return ans

    def hasNext(self) -> bool:
        return self.has_next

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

ans = []
itr = CombinationIterator("123456", 4)
while itr.hasNext():
    ans.append(itr.next())
print(len(ans))
print(*ans)




