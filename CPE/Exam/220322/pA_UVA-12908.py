""" UVA-12908: The book thief
    1. 模擬(Simulation) / 2. 二分搜尋(Binary Search)
    3. 數學(Math) https://zerojudge.tw/ShowThread?postid=34454&reply=0

    使用 Python 的話，以上三種方法在 CPE 和 ZeroJudge 上都可以 AC；
    但是前兩種方法在 UVA 上會 TLE ，只能使用第三種方法，並且開IO加速才能過。

    沒想到被 pA 搞破防，不過也成為 vjudge 上第一個用 Python 過這題的人了。
"""
def solve1(): # 1. Simulation
    while True:
        n = int(input())
        if n == 0:
            break
        i = 0
        s = 0
        while s <= n:
            i += 1
            s += i
        print(s-n, i)

from bisect import *
def solve2(): # 2. Binary Search
    MAX_S = 10 ** 8 + 5
    acc = [0]
    i = 0
    s = 0
    while s <= MAX_S:
        i += 1
        s += i
        acc.append(s)
    while True:
        n = int(input())
        if n == 0:
            break
        idx = bisect_right(acc, n)
        print(acc[idx] - n, idx)

"""
    3. Math
    n(n+1)/2 > s => n(n+1) > 2s => n^2 + n > 2s
     => n^2 + n + (1/2)^2 > 2s + (1/2)^2 (配方)
     => (n+(1/2))^2 > (8s+1)/4
     => n+(1/2) > sqrt(8s+1) / 2
     => n > (sqrt(8s+1) - 1) / 2
"""
import sys
def solve3():
    input = sys.stdin.readline
    def print(val):
        sys.stdout.write(str(val) + '\n')
    while True:
        s = int(input())
        if s == 0:
            break
        n = (int((8*s+1)**0.5) - 1) // 2 + 1 
        x = n * (n + 1) // 2 - s
        print(f"{x} {n}")
# solve1()
# solve2()
solve3()