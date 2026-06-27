from itertools import accumulate


def solve():
    N, S, K = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == N - 1

    ps = list(accumulate(A, initial=S))

    need = max(x - s for x, s in zip(A, ps))
    print(max(0, need) if need <= K else -1)


if __name__ == "__main__":
    solve()
