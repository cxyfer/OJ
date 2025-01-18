"""
    LeetCode 295. Find Median from Data Stream
"""

from heapq import *

hp1 = [] # Max Heap, <= median
hp2 = [] # Min Heap, > median

while True:
    try:
        x = int(input().strip())
    except EOFError:
        break

    if len(hp1) == len(hp2): # 當前數量為偶數，加入到左邊
        # 如果新加入的數字比右邊的最小值還要大，則先加入到右邊，再將右邊的最小值加入到左邊
        if hp2 and x > hp2[0]:
            heappush(hp1, -heappushpop(hp2, x))
        # 否則直接加入到左邊
        else:
            heappush(hp1, -x)
    else: # 當前數量為奇數，加入到右邊
        # 如果新加入的數字比左邊的最大值還要小，則先加入到左邊，再將左邊的最大值加入到右邊
        if x < -hp1[0]:
            heappush(hp2, -heappushpop(hp1, -x))
        # 否則直接加入到右邊
        else:
            heappush(hp2, x)

    # 如果兩邊數量相同，則中位數為兩邊堆頂的平均值
    if len(hp1) == len(hp2):
        print((-hp1[0] + hp2[0]) // 2)
    # 否則中位數為左邊堆頂的值
    else:
        print(-hp1[0])

