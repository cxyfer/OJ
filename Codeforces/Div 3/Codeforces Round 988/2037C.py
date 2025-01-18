from itertools import pairwise

MAX_N = int(4e5 + 5)
is_prime = [True] * (MAX_N)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX_N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N, i):
            is_prime[j] = False

t = int(input())
for _ in range(t):
    n = int(input())
    if n < 5:
        print(-1)
        continue
    odds, evens = [], []
    for i in range(1, n + 1):
        if i & 1:
            odds.append(i)
        else:
            evens.append(i)
    odds.sort(reverse=True)

    last_even = evens[-1]
    flag1 = False
    for i, odd in enumerate(odds):
        s = last_even + odd
        if s >= 4 and not is_prime[s]:
            if i != 0:
                odds[0], odds[i] = odds[i], odds[0]
            flag1 = True
            break
    if not flag1:
        print(-1)
        continue

    ans = evens + odds
    for x, y in pairwise(ans):
        s = x + y
        if s < 4 or is_prime[s]:
            print(-1)
            break
    else:
        print(*ans)