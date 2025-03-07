2#
# @lc app=leetcode.cn id=2671 lang=python3
#
# [2671] 频率跟踪器
#
from collections import defaultdict
# @lc code=start
class FrequencyTracker:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq[self.cnt[number]] -= 1 
        self.cnt[number] += 1
        self.freq[self.cnt[number]] += 1 

    def deleteOne(self, number: int) -> None:
        if self.cnt[number] > 0:
            self.freq[self.cnt[number]] -= 1
            self.cnt[number] -= 1
            self.freq[self.cnt[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0
    
# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
# @lc code=end

