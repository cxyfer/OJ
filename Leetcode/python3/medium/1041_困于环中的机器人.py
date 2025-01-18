#
# @lc app=leetcode.cn id=1041 lang=python3
#
# [1041] 困于环中的机器人
#

# @lc code=start
class Solution:
    """
        Simulation
        機器人想要擺脫循環，在壹串指令之後的狀態，必須是不位於原點且方向朝北。
    """
    def isRobotBounded(self, instructions: str) -> bool:
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir = 0 # 0: N, 1: E, 2: S, 3: W
        x = y = 0

        for inst in instructions:
            if inst == 'G':
                x += DIR[dir][0]
                y += DIR[dir][1]
            elif inst == 'L':
                dir = (dir - 1) % 4
            else:
                dir = (dir + 1) % 4
        return (x == 0 and y == 0) or dir != 0
# @lc code=end

