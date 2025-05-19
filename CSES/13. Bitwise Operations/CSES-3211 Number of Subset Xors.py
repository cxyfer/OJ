n = int(input())
A = list(map(int, input().split()))

BITS = 30
basis = [0] * (BITS + 1)

for x in A:
    for b in range(BITS, -1, -1):
        if (x >> b) & 1 == 0:
            continue

        if basis[b] == 0:
            basis[b] = x
            break

        x ^= basis[b]

print(2 ** sum(1 for x in basis if x != 0))