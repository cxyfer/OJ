# @algorithm @lc id=1354 lang=python3 
# @title find-players-with-zero-or-one-losses


from en.Python3.mod.preImport import *
# @test([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])=[[1,2,10],[4,5,7,8]]
# @test([[2,3],[1,3],[5,4],[6,4]])=[[1,2,5,6],[]]
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[], []]
        cnt = defaultdict(int)
        for x, y in matches:
            cnt[x] = cnt[x]
            cnt[y] += 1

        for k in sorted(cnt.keys()):
            if cnt[k] == 0:
                ans[0].append(k)
            elif cnt[k] == 1:
                ans[1].append(k)
        return ans
                
        