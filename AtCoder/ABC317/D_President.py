N = int(input())  
# DP 
MAX_ZSUM = 10**5 # 所有席位的總數的邊界數量
# dp[i] 表示取得i個席位所需要的最少票數
dp = [0] + [float("inf")] * MAX_ZSUM

ZSUM = 0 # 記錄所有席位的總數
for _ in range(N):
  x,y,z = map(int,input().split())
  ZSUM += z 
  vote = max((y-x+1)//2, 0) # 贏下此選區所需要的票數
  for i in range(MAX_ZSUM-1, z-1, -1): # 由大到小更新，避免重複計算同一個選區
     dp[i] = min(dp[i], dp[i-z] + vote)

ans = min(dp[(ZSUM+1)//2:]) # 取得一半以上席位所需要的最少票數
print(ans)

exit()



N = int(input())    
XYZ = [list(map(int, input().split(" "))) for _ in range(N)]

XYZ.sort(key=lambda x: x[2], reverse=True)

# votes[i] 表示贏下第i個選區所需要的票數
# votes = [XYZ[i][1] - XYZ[i][0] for i in range(N) if XYZ[i][1] > XYZ[i][0]]
# print(votes)
# # DP
# # dp[i][j] 表示在前i個選區中，贏下j個選區，且席位>所有席位的一半，所需要的最少票數
# sumZ = sum([XYZ[i][2] for i in range(N)])
# targetZ = sumZ // 2 + 1 # 所有席位的一半
# dp = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]
# dp[0][0] = 0
# for i in range(1, N+1):
#     for j in range(i+1):
#         x, y, z = XYZ[i-1]
#         dp[i][j] = dp[i-1][j]
#         if j < votes[i-1]:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = min(dp[i-1][j], dp[i-1][j-votes[i-1]] + 1)

# Fractional Knapsack
sumZ = sum([XYZ[i][2] for i in range(N)])
targetZ = sumZ // 2 + 1 # 所有席位的一半

ans = 0
cur = sum([XYZ[i][2] for i in range(N) if XYZ[i][1] < XYZ[i][0]])
if cur >= targetZ:
    print(0)
    exit()

fracs = [XYZ[i] + [(XYZ[i][1] - XYZ[i][0]) / XYZ[i][2]]  for i in range(N) if XYZ[i][1] > XYZ[i][0]]
fracs.sort(key=lambda x: x[3])

for frac in fracs:
    x, y, z, f = frac
    if cur >= targetZ:
        break
    cur += z
    ans += (y-x) // 2 +1
# 特判?
cur = sum([XYZ[i][2] for i in range(N) if XYZ[i][1] < XYZ[i][0]])
diffs = [XYZ[i] + [(XYZ[i][1] - XYZ[i][0])]  for i in range(N) if XYZ[i][1] > XYZ[i][0]]
diffs.sort(key=lambda x: x[3])
ans2 = 0
for diff in diffs:
    x, y, z, d = diff
    if cur >= targetZ:
        break
    cur += z
    ans2 += (y-x) // 2 +1
print(min(ans, ans2))

