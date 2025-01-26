n = int(input())
A = list(map(int, input().split()))

pos = [[] for _ in range(n + 1)]
for i, x in enumerate(A, start=1):
    pos[x].append(i)

# 不包含 lst 中所有位置的區間數量
def f(lst):
    res = 0
    lst = [0] + lst + [n + 1]
    for i in range(1, len(lst)):
        cnt = lst[i] - lst[i - 1] - 1  # (lst[i-1], lst[i]) 中的元素數量，是左開右開的區間
        res += cnt * (cnt + 1) // 2
    return res

# 包含 x 但不包含 x - 1 的區間數量
def g(x):
    return f(pos[x - 1]) - f(sorted(pos[x - 1] + pos[x]))

ans = 0
for i in range(1, n + 1):
    ans += g(i)
print(ans)

# from random import *

# for _ in range(100):
#     n = randint(10, 20)
#     m = randint(5, n - 5)
#     lst = sample(range(1, n + 1), k=m)
#     lst.sort()

#     def f(lst):
#         res = 0
#         lst = [0] + lst + [n + 1]
#         for i in range(1, len(lst)):
#             cnt = lst[i] - lst[i - 1] - 1
#             res += cnt * (cnt + 1) // 2
#         return res

#     def f2(lst):
#         res = 0
#         lst = [0] + lst + [n + 1]
#         for i in range(1, len(lst)):
#             cnt = lst[i] - lst[i - 1]
#             res += cnt * (cnt + 1) // 2
#         return res

#     if f(lst) != f2(lst):
#         print(n, m)
#         print(*lst)
#         break
