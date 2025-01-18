from heapq import heappop, heappush

N = 1500
primes = [2, 3, 5]

visited = set()
hp = [1]
for _ in range(N):
    ans = heappop(hp)
    for p in primes:
        new_ans = ans * p
        if new_ans not in visited:
            visited.add(new_ans)
            heappush(hp, new_ans)

print(f"The 1500'th ugly number is {ans}.")