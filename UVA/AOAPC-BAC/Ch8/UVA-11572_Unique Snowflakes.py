import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val) + "\n")

from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    A = [int(input()) for _ in range(n)]

    ans = left = 0
    cnt = defaultdict(int)
    for right, x in enumerate(A):
        cnt[x] += 1
        while cnt[x] > 1:
            cnt[A[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)
    print(ans)