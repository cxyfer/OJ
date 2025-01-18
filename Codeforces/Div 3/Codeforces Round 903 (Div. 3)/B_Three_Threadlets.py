from collections import Counter
t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    lst = [a, b, c]
    lst.sort()
    # print(i+1)
    ans = "NO"
    for r in range(3):
        for idx in range(1, len(lst)):
            if lst[idx] - lst[0] != 0:
                lst.append(lst[idx] - lst[0])
                lst[idx] = lst[0]
        
        if len(lst) == Counter(lst).most_common()[0][1] and len(lst) <= 6:
            ans = "YES"
            break
    print(ans)
