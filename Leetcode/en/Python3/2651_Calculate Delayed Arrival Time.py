# @algorithm @lc id=2748 lang=python3 
# @title calculate-delayed-arrival-time


from en.Python3.mod.preImport import *
# @test(15,5)=20
# @test(13,11)=0
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24