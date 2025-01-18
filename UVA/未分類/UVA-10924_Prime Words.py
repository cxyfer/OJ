MAXN = int(1e4) + 5
is_prime = [True] * MAXN
# is_prime[0] = is_prime[1] = False # 這題把 1 當質數
for i in range(2, MAXN):
    if is_prime[i]:
        for j in range(i * i, MAXN, i):
            is_prime[j] = False

while True:
    try:
        s = input().strip()
    except EOFError:
        break
    d = 0
    for ch in s:
        if ch.isupper():
            d += ord(ch) - ord('A') + 27
        elif ch.islower():
            d += ord(ch) - ord('a') + 1
    if is_prime[d]:
        print("It is a prime word.")
    else:
        print("It is not a prime word.")