# 8015. Furthest Point From Origin
# You are given a string moves of length n consisting only of characters 'L', 'R', and '_'. The string represents your movement on a number line starting from the origin 0.

# In the ith move, you can choose one of the following directions:

# move to the left if moves[i] = 'L' or moves[i] = '_'
# move to the right if moves[i] = 'R' or moves[i] = '_'
# Return the distance from the origin of the furthest point you can get to after n moves.
from collections import Counter

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt = Counter(moves)
        return abs(cnt['L'] - cnt['R']) + cnt['_']