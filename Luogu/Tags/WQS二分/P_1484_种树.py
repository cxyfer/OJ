from heapq import heappush, heappop

# fmt: off
import sys
it = iter(sys.stdin.read().split())
def input(n: int = 1):
    return (next(it) for _ in range(n))
# fmt: on


def solve1():
    n, k = map(int, input(2))
    A = list(map(int, input(n)))

    INF = int(1e18)
    A = [-INF] + A + [-INF]
    L = [i - 1 for i in range(n + 2)]
    R = [i + 1 for i in range(n + 2)]
    L[0] = 0
    R[n + 1] = n + 1
    alive = [True] * (n + 2)

    hp = []
    for i, x in enumerate(A):
        heappush(hp, (-x, i))

    ans = acc = 0
    for _ in range(k):
        while hp:
            x, i = heappop(hp)
            if not alive[i]:
                continue
            x = -x
            acc += x
            ans = max(ans, acc)

            l, r = L[i], R[i]
            y = A[l] + A[r] - x
            A[i] = y
            alive[l] = alive[r] = False
            # 注意更新順序，LHS 需要先更新使用到 L[i] 的 R[L[L[i]]] 後，才能更新 L[i]
            # R[L[L[i]]], L[i] = i, L[L[i]]
            # L[R[R[i]]], R[i] = i, R[R[i]]
            # 當然先保存 l = L[i], r = R[i] 會比較不會出錯
            L[i], R[L[l]] = L[l], i
            R[i], L[R[r]] = R[r], i
            heappush(hp, (-y, i))
            break

    print(ans)


def solve2():
    n, k = map(int, input(2))
    A = list(map(int, input(n)))

    """WQS Binary Search (Aliens Trick)"""

    def check(p: int):
        f0, f1 = (0, 0), (float("-inf"), 0)  # 不選/選 當前元素
        for x in A:
            f0, f1 = max(f0, f1), (f0[0] + x - p, f0[1] + 1)
        return max(f0, f1)

    mx = max(A)
    left, right = 0, mx
    while left <= right:
        mid = (left + right) // 2
        _, cnt = check(mid)
        if cnt <= k:
            right = mid - 1
        else:
            left = mid + 1

    ans = check(left)[0] + left * k
    if right >= 0:
        ans = min(ans, check(right)[0] + right * k)
    print(ans)


# solve = solve1
solve = solve2

if __name__ == "__main__":
    solve()
