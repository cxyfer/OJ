from bisect import *

n = int(input())
A = list(map(int, input().split()))

tail = [A[0]] # tail[i] 表示 長度為 i+1 的 LIS 的最後一個元素的最小值，初始化 tail[0] = A[0]

for i in range(1, n):
    if A[i] > tail[-1]: # nums[i] 可以接在 tail 的末尾，並構成更長的 LIS
        tail.append(A[i]) # tail 長度加 1
        continue

    # 在 tail 中二分查找，找到第一個大於等於 A[i] 的元素，並將其更新為 A[i]
    left = bisect_left(tail, A[i])
    tail[left] = A[i]

print(len(tail))