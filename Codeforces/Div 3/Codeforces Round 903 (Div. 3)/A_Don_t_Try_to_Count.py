t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()
    ans = 0
    # print(s, x)
    while x.find(s) == -1 and (len(x) <= 2 * m or ans == 0):
        x *= 2
        ans += 1
        # print(s, x)
    print(ans if x.find(s) != -1 else -1)
