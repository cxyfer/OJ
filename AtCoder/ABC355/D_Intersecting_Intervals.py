

N = int(input())
L, R = [], []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
L.sort()
R.sort()

"""
    Binary Search
    O(N log N)
"""
# from bisect import *
# ans = N * (N - 1) // 2 
# for x in L:
#     ans -= bisect_left(R, x)
# print(ans)

"""
    Two Pointers
    O(N)
"""
ans = N * (N - 1) // 2 
j = 0
for i, x in enumerate(L):
    while j < N and R[j] < x:
        j += 1
    ans -= j
print(ans)