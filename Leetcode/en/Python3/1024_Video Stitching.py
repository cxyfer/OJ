# @algorithm @lc id=1081 lang=python3 
# @title video-stitching


from en.Python3.mod.preImport import *
# @test([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]],10)=3
# @test([[0,1],[1,2]],5)=-1
# @test([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],9)=3
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        """
            Greedy
            轉換成造橋問題
            https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/solutions/2123855/yi-zhang-tu-miao-dong-pythonjavacgo-by-e-wqry/
            Similar to 45. Jump Game II
            Similar to 1326. Minimum Number of Taps to Open to Water a Garden
        """
        n = len(clips)
        rightmost = [0] * (time) # rightmost[i] 表示從第i秒可以覆蓋到的最遠距離
        for i, (L ,R) in enumerate(clips): # L表示左端點，R表示右端點
            if L < time:
                rightmost[L] = max(rightmost[L], R)

        ans = 0 # 答案，需要合併的數量(跳躍次數)
        cur = 0 # 已合併的區間的右端點
        nxt = 0 # 下一個區間的右端點
        for i in range(time):
            nxt = max(nxt, rightmost[i])
            if i == cur: # 到達當前能合併的最遠位置
                if i == nxt: # 到達「可」合併的最遠位置，即無論怎麼合併，都無法從i到i+1了
                    return -1
                cur = nxt # 再合併一個區間
                ans += 1
        return ans