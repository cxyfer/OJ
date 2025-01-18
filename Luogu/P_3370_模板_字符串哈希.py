from random import randint

MOD = 1070777777
BASE = randint(233, 2333)

n = int(input())
st = set()
for _ in range(n):
    s = input()
    n = len(s)
    P = [1] + [0] * n
    H = [0] * (n + 1)
    for i, b in enumerate(s):
        P[i + 1] = P[i] * BASE % MOD
        H[i + 1] = (H[i] * BASE + ord(b)) % MOD
    st.add(H[-1])
print(len(st))