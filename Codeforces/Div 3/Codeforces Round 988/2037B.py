from collections import defaultdict

# MAX_N = int(2e5 + 5)

# is_prime = [True] * MAX_N
# is_prime[0] = is_prime[1] = False
# factors = [[1] for _ in range(MAX_N)]
# for i in range(2, int(MAX_N ** 0.5) + 1):
#     if is_prime[i]:
#         for j in range(i * i, MAX_N, i):
#             is_prime[j] = False
#             factors[j].append(i)

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    cnt = defaultdict(int)
    for x in A:
        cnt[str(x)] += 1

    k = n - 2
    # for a in factors[k]:
    #     b = k // a
    #     if a == b and cnt[str(a)] >= 2 or a != b and cnt[str(a)] > 0 and cnt[str(b)] > 0:
    #         print(a, b)
    #         break
    # else:
    #     print(-1)
    for a in A:
        b, r = divmod(k, a)
        if r != 0:
            continue
        if a == b and cnt[str(a)] >= 2 or a != b and cnt[str(a)] > 0 and cnt[str(b)] > 0:
            print(a, b)
            break
    else:
        print(-1)
