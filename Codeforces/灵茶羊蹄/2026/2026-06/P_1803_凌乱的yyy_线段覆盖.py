# fmt: off
import sys
it = iter(sys.stdin.read().splitlines())
def input():
    return next(it)
def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)
# fmt: on


def solve():
    n = int(input())
    segs = [tuple(map(int, input().split())) for _ in range(n)]
    segs.sort(key=lambda x: (x[1]))

    ans = 0
    last = -1
    for l, r in segs:
        if l >= last:
            ans += 1
            last = r
    print(ans)


if __name__ == "__main__":
    solve()
