def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    mx = -1
    ans = cnt = 0
    for i, x in enumerate(A, 1):
        if x > mx:
            mx = x
            ans = i
            cnt = 1
        elif x == mx:
            cnt += 1
    print(ans if cnt == 1 else -1)


if __name__ == "__main__":
    solve()
