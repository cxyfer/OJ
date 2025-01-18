class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if k >= n:
            return max(range(n), key=lambda i: skills[i])
        ans = 0
        win = 0
        for i in range(1, n):
            if skills[i] > skills[cur]:
                cur = i
                win = 0
            win += 1
            if win == k:
                break
        return ans