import sys
input = sys.stdin.readline
def ans(*args):
    print(*args if len(args) else "!", flush=True)
    return int(input())

t = int(input())
for _ in range(t):
    n = int(input())
    ans("add", -1)
    ans("mul", 999999999)
    ans("add", 999999999)
    ans("digit")
    ans("add", n - 81)
    ans()