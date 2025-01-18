n, m = map(int, input().split())
mp = dict()
for _ in range(n):
    a, b = input().split()
    mp[a] = b
for _ in range(m):
    s = input()
    n = len(s)
    if s in mp:
        print(mp[s])
    elif n > 1 and s[-1] == "y" and s[-2] not in "aeiou":
        print(s[:-1] + "ies")
    elif s[-1] in "osx" or s[-2:] in ["ch", "sh"]:
        print(s + "es")
    else:
        print(s + "s")