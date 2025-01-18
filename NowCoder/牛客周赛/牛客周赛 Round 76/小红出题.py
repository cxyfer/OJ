n = int(input())
q, r = divmod(n, 7)
print((q * 5 + min(r, 5)) * 3)