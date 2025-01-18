from collections import Counter
N = 2005
is_prime = [True] * N
is_prime[0] = is_prime[1] = False
for i in range(2, N):
    if is_prime[i]:
        for j in range(i*i, N, i):
            is_prime[j] = False

t = int(input())
for kase in range(1, t+1):
    s = input()
    cnt = Counter(s)
    ans = [k for k, v in sorted(cnt.items()) if is_prime[v]]
    print(f"Case {kase}: {''.join(ans) if ans else 'empty'}")