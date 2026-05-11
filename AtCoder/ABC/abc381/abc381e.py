from bisect import bisect_left, bisect_right
from collections import defaultdict
from itertools import accumulate


def solve():
    n, q = map(int, input().split())
    s = input()
    assert len(s) == n

    pos = defaultdict(list)
    for i, ch in enumerate(s, start=1):
        pos[ch].append(i)

    ss = list(accumulate(map(lambda ch: ch == "/", s), initial=0))

    for _ in range(q):
        l, r = map(int, input().split())

        if ss[r] - ss[l - 1] == 0:
            print(0)
            continue

        def check(mid: int) -> bool:
            idx1 = bisect_left(pos["1"], l) + mid - 1
            idx2 = bisect_right(pos["2"], r) - mid
            if idx1 >= len(pos["1"]) or idx2 < 0:
                return False
            ll, rr = pos["1"][idx1], pos["2"][idx2]
            return ss[rr] - ss[ll - 1] > 0

        left, right = 1, r - l + 1
        while left <= right:
            mid = (left + right) >> 1
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        print(1 + (right << 1))


if __name__ == "__main__":
    solve()
