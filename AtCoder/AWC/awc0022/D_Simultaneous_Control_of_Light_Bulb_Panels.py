def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    diff = [0] * N
    ans = s = 0
    for i, x in enumerate(A):
        s ^= diff[i]
        if x ^ s == 1:
            if i <= N - K:
                ans += 1
                s ^= 1
                if i + K < N:
                    diff[i + K] ^= 1
            else:
                ans = -1
                break
    print(ans)


if __name__ == "__main__":
    solve()
