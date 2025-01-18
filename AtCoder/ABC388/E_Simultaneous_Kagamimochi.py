"""
Greedy + Binary Search

如果可以組成 k 對，則基於貪心原則：
- 在上面的 k 個麻糬是最小的 k 個
- 在下面的 k 個麻糬是最大的 k 個

因此可以在 O(k) 時間內檢查是否可以組成 k 對，故可以對 k 進行二分搜尋。
k 的範圍是 [0, N//2]，整體時間複雜度為 O(N log N)。
"""

# N = int(input())
# A = list(map(int, input().split()))

# # 是否可以組成 k 對麻糬
# def check(k):
#     for i in range(k):
#         if A[i] * 2 > A[N - k + i]:
#             return False
#     return True

# # 二分搜尋
# left, right = 0, N // 2
# while left <= right:
#     mid = (left + right) // 2
#     if check(mid):
#         left = mid + 1
#     else:
#         right = mid - 1
# print(right)  # 越小越合法，求最大的合法值

N = int(input())
A = list(map(int, input().split()))

# 計算下一個符合條件的位置
nxt = [0] * N
right = 0
for i in range(N):
    while right < N and 2 * A[i] > A[right]:
        right += 1
    nxt[i] = right

# 計算每個位置與下一個符合條件的位置的間距
gaps = [nxt[i] - i for i in range(N)]
pre = [0] * N
pre[0] = gaps[0]
for i in range(1, N):
    pre[i] = max(pre[i - 1], gaps[i])

# 是否可以組成 k 對麻糬
def check(k):
    return k - 1 + pre[k - 1] <= N - 1

# 二分搜尋
left, right = 0, N // 2
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)  # 越小越合法，求最大的合法值