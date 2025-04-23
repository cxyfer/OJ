#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    obstacles = set((x, y) for x, y in obstacles)
    ans = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            x, y = r_q + dx, c_q + dy
            while 1 <= x <= n and 1 <= y <= n and (x, y) not in obstacles:
                ans += 1
                x, y = x + dx, y + dy
    return ans