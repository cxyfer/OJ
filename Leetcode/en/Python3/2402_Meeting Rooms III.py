# @algorithm @lc id=2479 lang=python3 
# @title meeting-rooms-iii


from en.Python3.mod.preImport import *
# @test(2,[[0,10],[1,5],[2,7],[3,4]])=0
# @test(3,[[1,20],[2,10],[3,5],[4,9],[6,8]])=1
class Solution:
    """
        Simulation + Heap
    """
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort() # 依照會議開始時間排序
        cnt = [0] * (n) # 每個會議室的使用次數
        hp = [(0, i) for i in range(n)] # 維護每個會議室的結束時間，初始化為0，表示每個會議室在時間0時都是可用的
        for st, ed in meetings:
            d = ed - st # 會議持續時間
            while hp and hp[0][0] < st: # 為滿足規則1，可將該會議室的結束時間更新為當前會議的開始時間
                _, tmp_idx = heappop(hp)
                heappush(hp, (st, tmp_idx))
            t, idx = heappop(hp) # 取出最早結束的會議室編號
            ed = t + d # 更新該會議室的結束時間
            heappush(hp, (ed, idx)) # 將該會議的結束時間和使用的會議室編號加入heap
            cnt[idx] += 1
        ans = 0
        for i, v in enumerate(cnt):
            if v > cnt[ans]:
                ans = i
        return ans