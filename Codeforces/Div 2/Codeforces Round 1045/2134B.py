"""
2134B - Add 0 or K
https://codeforces.com/contest/2134/problem/B
構造

賽時寫法：
考慮三種情況：
1. k 是奇數，此時顯然可以把 A[i] 湊成偶數，gcd 至少為 2
2. 考慮把 A[i] 湊成 k - 1 的倍數，每次 +k 可以讓餘數 +1，直到餘數為 k - 1 為止
3. 但 k = 2 時需要特判，此時湊成 3 的倍數

簡潔寫法：
直接湊成 k + 1 的倍數，每次 +k 可以讓餘數 -1，直到餘數為 0 為止
"""
# from math import gcd
# from functools import reduce

def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    # if k & 1:  # gcd >= 2
    #     for i, x in enumerate(A):
    #         if x & 1:
    #             A[i] += k
    # elif k == 2:
    #     for i, x in enumerate(A):
    #         r = x % 3
    #         if r == 1:
    #             A[i] += k
    #         elif r == 2:
    #             A[i] += 2 * k
    # else:
    #     for i, x in enumerate(A):
    #         r = x % (k - 1)
    #         if r != 0:
    #             A[i] += (k - r - 1) * k
    for i, x in enumerate(A):
        r = x % (k + 1)
        A[i] += r * k
    print(*A)
    # assert reduce(gcd, A) >= 2, A

t = int(input())
for _ in range(t):
    solve()