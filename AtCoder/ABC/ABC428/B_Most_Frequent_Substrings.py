from collections import Counter


def solve():
    N, K = map(int, input().split())
    S = input()

    cnt = Counter(S[i : i + K] for i in range(N - K + 1))
    mx = max(cnt.values())
    print(mx)
    print(*sorted(k for k, v in cnt.items() if v == mx))


if __name__ == "__main__":
    solve()
