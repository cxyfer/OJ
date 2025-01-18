from functools import cache

@cache
def dfs(n: str) -> int:
    s = sum([int(ch) for ch in n])
    if len(n) == 1 and s != 9:
        return -0x3f3f3f3f
    if s == 9:
        return 1
    return 1 + dfs(str(s))

while True:
    n = input()
    if n == "0":
        break
    dfs(n)
    ans = dfs(n)
    if ans < 0:
        print(f"{n} is not a multiple of 9.")
    else:

        print(f"{n} is a multiple of 9 and has 9-degree {ans}.")