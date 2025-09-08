s = input()

n = len(s)
f = [0] * (n + 1)
for i, c in enumerate(s, start=1):
    v = ord(c) - ord('a') + 1
    f[i] = max(f[i - 1], f[i - 2] + v)
print(f[n])