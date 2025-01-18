from bisect import *

fib = [0, 1]
while fib[-1] < 1e8:
    fib.append(fib[-1] + fib[-2])
T = int(input())

for _ in range(T):
    n = int(input())
    tmp = n

    ans = ""
    idx = bisect_right(fib, n) - 1
    for i in range(idx, 1, -1):
        if tmp >= fib[i]:
            tmp -= fib[i]
            ans += "1"
        else:
            ans += "0"
    print(f"{n} = {ans} (fib)")
