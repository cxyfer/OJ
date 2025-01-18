# @algorithm @lc id=1184 lang=python3 
# @title car-pooling


from en.Python3.mod.preImport import *
# @test([[2,1,5],[3,3,7]],4)=false
# @test([[2,1,5],[3,3,7]],5)=true
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        MAX_TO = max([trip[2] for trip in trips])

        diff = [0] * (MAX_TO + 1)
        for num, x, y in trips:
            diff[x] += num # from 
            diff[y] -= num # to
        
        cnt = 0 # 當前車上的人數
        for i in range(MAX_TO + 1):
            cnt += diff[i]
            if cnt > capacity: # 超載
                return False
        return True