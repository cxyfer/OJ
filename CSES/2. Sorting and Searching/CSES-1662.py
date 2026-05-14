from collections import defaultdict
from random import randint

U = (1 << 64) - 1


class Wrapper:
    BASE = randint(1, U)

    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value ^ self.BASE)

    def __eq__(self, other):
        return isinstance(other, Wrapper) and self.value == other.value


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    ans = s = 0
    cnt = defaultdict(int)
    cnt[Wrapper(0)] = 1
    for x in A:
        s = (s + x) % n
        ans += cnt[Wrapper(s)]
        cnt[Wrapper(s)] += 1
    print(ans)


if __name__ == "__main__":
    solve()
