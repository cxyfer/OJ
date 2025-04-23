#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

from bisect import *
def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked = list(sorted(set(ranked)))
    n = len(ranked)
    ans = []
    for i, p in enumerate(player):
        idx = bisect_right(ranked, p)
        ans.append(n - idx + 1)
    return ans

if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))
