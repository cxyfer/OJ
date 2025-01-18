from itertools import *

WEEKDAY = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
pre_sum = list(accumulate(DAYS, initial=0)) # prefix sum
base = 5 # 2011/1/1 is Saturday, so start at Friday

T = int(input())
for _ in range(T):
    m, d = map(int, input().split())
    day = (base + pre_sum[m-1] + d) % 7
    print(WEEKDAY[day])