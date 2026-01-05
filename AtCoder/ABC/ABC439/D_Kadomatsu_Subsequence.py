from collections import defaultdict

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    def do(A):
        ans = 0
        pre3 = defaultdict(int)
        pre7 = defaultdict(int)
        for x in A:
            if x % 5 == 0:
                v = x // 5
                ans += pre7[v] * pre3[v]
            if x % 3 == 0:
                pre3[x // 3] += 1
            if x % 7 == 0:
                pre7[x // 7] += 1
        return ans

    print(do(A) + do(A[::-1]))

if __name__ == "__main__":
    solve()