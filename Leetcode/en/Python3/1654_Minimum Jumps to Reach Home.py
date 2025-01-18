# @algorithm @lc id=1757 lang=python3 
# @title minimum-jumps-to-reach-home


from en.Python3.mod.preImport import *
# @test([14,4,18,1,15],3,15,9)=3
# @test([8,3,16,6,12,20],15,13,11)=-1
# @test([1,6,2,14,5,17,4],16,9,7)=2
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # BFS
        if x == 0: return 0
        """
            本題的關鍵是最遠可以跳到的位置為 max(f + a + b, x + b)，否則會TLE或MLE
            大神的證明：https://leetcode.cn/problems/minimum-jumps-to-reach-home/solutions/485685/dao-jia-de-zui-shao-tiao-yue-ci-shu-zui-duan-lu-zh/
        """
        max_pos = max(max((forbidden)) + a + b, x + b) # 最遠可以跳到的位置
        forbidden = set(forbidden)
        visited = set([(0, False)]) # (pos, back_jump)，記錄訪問過的位置，每個位置都有2個方向
        queue = deque([(0, False, 0)]) # (pos, back_jump, step)
        while queue:
            pos, back_jump, step = queue.popleft()
            nxt = pos + a # 往前跳
            if nxt <= max_pos and nxt not in forbidden and (nxt, False) not in visited:
                if nxt == x:
                    return step + 1
                visited.add((nxt, False))
                queue.append((nxt, False, step + 1))
            nxt = pos - b # 往後跳
            if not back_jump and nxt > 0 and nxt not in forbidden and (nxt, True) not in visited:
                if nxt == x:
                    return step + 1
                visited.add((nxt, True))
                queue.append((nxt, True, step + 1))
        return -1