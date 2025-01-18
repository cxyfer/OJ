"""
Reference:
- https://www.bilibili.com/video/BV1RTS6YPEvs/
- https://codeforces.com/contest/2036/submission/289710176
"""
import sys
input = sys.stdin.readline

def query(l, r):
    print('xor', l, r, flush=True)
    return int(input())

def answer(a, b, c):
    print('ans', a, b, c, flush=True)

t = int(input())
for _ in range(t):
    n = int(input())

    s = query(1, n)
    if s != 0:
        l, r = 1, n
        while l <= r:
            mid = (l + r) >> 1
            if query(mid, n) == s:
                l = mid + 1
            else:
                r = mid - 1
        a = r
    else: # a ^ b ^ c = 0
        for i in range(1, n.bit_length()):
            res = query(1, (1 << i) - 1)
            if res != 0:
                a = res
                break
    l, r = a + 1, n
    while l <= r:
        mid = (l + r) >> 1
        if query(1, mid) == s:
            r = mid - 1
        else:
            l = mid + 1
    c = l
    b = s ^ a ^ c
    answer(a, b, c)