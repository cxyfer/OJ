from heapq import *

n, m, k = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
hp = [-x for x in A]  # Max Heap
heapify(hp)

"""
基於貪心思想，應盡可能的把大的數字變小

維護一個 Max Heap，每次從堆頂取出一個數，進行操作：
- 對於偶數，如果還能做操作1，則可以除以二，並將結果放回堆中
- 對於奇數，需要分兩種情況
    - 如果還能做操作1和操作2，則可以減一後除以二，並將結果放回堆中
    - 如果只能做操作1，則表示之後無法再操作奇數，可以直接累加到答案中。
- 若最後仍有剩餘的操作2次數，則可以應用於剩餘的奇數上。

時間複雜度：O(N \log U \log N)，其中 U 是 A 中的最大值。
- 每個數字最多被操作 O(\log U) 次，總共 N 個數字，每次操作需要 O(\log N) 時間。
"""

while hp and m > 0:
    x = -heappop(hp)
    if x == 0:  # 剩下的數都是 0，可以終止
        break
    if x % 2 == 0:
        heappush(hp, -(x // 2))
        m -= 1
    else:
        if k > 0:
            heappush(hp, -(x - 1))
            k -= 1
        else:
            ans += x
o = sum((-x) & 1 for x in hp)
print(ans + sum(-x for x in hp) - min(o, k))