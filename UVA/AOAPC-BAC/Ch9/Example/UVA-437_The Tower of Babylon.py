"""
    DP：LIS (Longest Increasing Subsequence)
    每種積木的數量不限，且每種積木有六種擺放方式，
    故可以將所有積木的六種擺放方式排序後，求 LIS
    令 dp[i] 表示以第 i 個積木為最後一個積木(最下面)時的最大高度
    tags: DP, LIS, 紫書, CPE-171219, CPE-211019, CPE-221018
"""
kase = 1
while True:
    n = int(input())
    if n == 0:
        break
    blocks = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        blocks.append((x, y, z))
        blocks.append((x, z, y))
        blocks.append((y, x, z))
        blocks.append((y, z, x))
        blocks.append((z, x, y))
        blocks.append((z, y, x))
    blocks.sort(key = lambda x: (x[0], x[1], x[2]))
    dp = [0] * (6 * n)
    for i, (x, y, z) in enumerate(blocks):
        dp[i] = z
        for j in range(i): # i 可以接在 j 後面 ( i 在下面)
            if x > blocks[j][0] and y > blocks[j][1]: 
                dp[i] = max(dp[i], dp[j] + z)
    print(f"Case {kase}: maximum height = {max(dp)}")
    kase += 1
