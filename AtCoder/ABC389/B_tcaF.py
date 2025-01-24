from bisect import bisect_left

fact = [1]
while fact[-1] < 3e18 + 5:
    fact.append(fact[-1] * len(fact))

X = int(input())
print(bisect_left(fact, X))

# X = int(input())
# ans = f = 1
# while f != X:
#     ans += 1
#     f *= (ans)
# print(ans)