# @algorithm @lc id=1627 lang=python3 
# @title last-moment-before-all-ants-fall-out-of-a-plank


from en.Python3.mod.preImport import *
# @test(4,[4,3],[0,1])=4
# @test(7,[],[0,1,2,3,4,5,6,7])=7
# @test(7,[0,1,2,3,4,5,6,7],[])=7
class Solution:
    """
        Similar to 2731. Movement of Robots
    """
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # ans = 0
        # for pos in left:
        #     ans = max(ans, pos)
        # for pos in right:
        #     ans = max(ans, n-pos)
        # return ans
        return max(max(left + [0]), n-min(right + [n]))