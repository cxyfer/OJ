from functools import cache

@cache
def dfs(n: str) -> int:
    s = sum([int(ch) for ch in n])
    if len(n) == 1 and s != 9:
        return -float('inf')
    if s == 9:
        return 1
    return 1 + dfs(str(s))

while True:
    n = input()
    if n == "0":
        break
    ans = dfs(n)
    if ans == -float('inf'):
        print(f"{n} is not a multiple of 9.")
    else:
        print(f"{n} is a multiple of 9 and has 9-degree {ans}.")