# """
#     首先做前綴和 s ，如此便可以把區間和轉換為兩個前綴的差。
#     之後，對於每個固定的右端點 right ，我們想要使得 s[right] - s[left] 最大，因此我們可以找到一個最小的 s[left]
#     故只需要維護最小的 s[left] 即可
# """
# n = int(input())
# X = list(map(int, input().split()))

# ans = float('-inf')
# s = mn = 0
# for i in range(n):
#     s += X[i] # 前綴和
#     ans = max(ans, s - mn) # 更新答案
#     mn = min(mn, s) # 更新最小值
# print(ans)

"""
    DP 解法
"""
n = int(input())
S = list(map(int, input().split()))

ans = cur = S[0]
for i in range(1, n):
    cur = max(cur + S[i], S[i])
    ans = max(ans, cur)
print(ans)