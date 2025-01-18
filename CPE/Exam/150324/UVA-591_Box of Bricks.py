from itertools import count

for kase in count(1):
    n = int(input().strip())
    if n == 0:
        break
    bricks = list(map(int, input().strip().split()))
    avg = sum(bricks) // n
    ans = sum(abs(x - avg) for x in bricks) // 2

    print(f"Set #{kase}")
    print(f"The minimum number of moves is {ans}.")
    print()