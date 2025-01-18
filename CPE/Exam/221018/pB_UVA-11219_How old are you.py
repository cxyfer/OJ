t = int(input())

for kase in range(1, t+1):
    input()
    d1, m1, y1 = map(int, input().split("/"))
    d2, m2, y2 = map(int, input().split("/"))
    print("Case #%d: " % kase, end="")

    if y1 < y2 or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 < d2):
        print("Invalid birth date")
    else:
        if m2 > m1 or (m2 == m1 and d2 > d1):
            age = y1 - y2 - 1
        else:
            age = y1 - y2
        if age > 130:
            print("Check birth date")
        else:
            print(age)