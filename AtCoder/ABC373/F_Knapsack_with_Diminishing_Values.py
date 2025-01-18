N, W = map(int, input().split())  
items = [list(map(int, input().split())) for _ in range(N)]  

# dp[i] 表示使用 i 的重量可以獲得的最大幸福值  
dp = [0] * (W + 1)  

for w, v in items:  
    for j in range(W, w - 1, -1):
        for k in range(1, v+1):
            if k * w > j:
                break
            happiness = k * v - k * k
            if dp[j] > dp[j - k * w] + happiness:
                break
            dp[j] = max(dp[j], dp[j - k * w] + happiness)
print(dp[W])


# data = []

# bag = [0] * (W + 1)
# # w, [v, v-1]
# for _ in range(N):
#     w, v = map(int, input().split())
#     for i in range(W - w + 1, -1, -1):
#         for j in range(1, v+1):
#             x = (i + j*w)
#             if x > W: break
#             if bag[x] > bag[i] + v*j-j*j:
#                 break
#             bag[x] = bag[i] + v*j-j*j
# print(bag[-1])
