import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

from collections import defaultdict

while True:
    n = int(input())
    if n == 0:
        break

    cnt = defaultdict(int)
    for _ in range(n):
        a, b = map(int, input().split())
        cnt[(a, b)] += 1

    for (a, b), v in cnt.items():
        if v != cnt[(b, a)]:
            print("NO")
            break
    else:
        print("YES")