def solve():
    N = int(input())
    L = list(map(int, input().split()))
    s1 = s2 = 1
    for i in range(N):
        if L[i] == 0:
            s1 += 1
        else:
            break
    for i in range(N - 1, -1, -1):
        if L[i] == 0:
            s2 += 1
        else:
            break
    print(N + 1 - min(s1 + s2, N + 1))

if __name__ == "__main__":
    solve()