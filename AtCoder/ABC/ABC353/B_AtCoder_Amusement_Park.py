"""
    Simulation
    Similar to LeetCode 2079. Watering Plants
"""
N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
cur = K
for Ai in A:
    if Ai > cur: # 空位不夠，先啟動一次
        ans += 1
        cur = K
    cur -= Ai
if cur != K:
    ans += 1
print(ans)