from bisect import *

n = int(input())
nums = list(map(int, input().split()))

tail = []
for i, x in enumerate(nums):
    j = bisect_right(tail, x) # 允許重複，所以用 bisect_right
    if j == len(tail):
        tail.append(x)
    else:
        tail[j] = x

print(len(tail))