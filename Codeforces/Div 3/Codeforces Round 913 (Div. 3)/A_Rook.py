N = int(input())

for tc in range(1, N+1):
    x, y = list(input())
    ans = [x + str(i)  for i in range(1, 9) if i != int(y)]
    ans += [chr(ord('a') + i) + y for i in range(8) if  ord('a') + i != ord(x)]
    print(*ans, sep="\n")
