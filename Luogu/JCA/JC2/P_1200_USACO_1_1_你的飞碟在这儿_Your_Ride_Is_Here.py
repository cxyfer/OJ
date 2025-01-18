s = input()
t = input()
MOD = 47
x = y = 1
for i, ch in enumerate(s):
    x = x * (ord(ch) - ord('A') + 1) % MOD
for i, ch in enumerate(t):
    y = y * (ord(ch) - ord('A') + 1) % MOD

print("GO" if x % MOD == y % MOD else "STAY")