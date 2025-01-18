from collections import Counter
t = int(input())

for _ in range(t):
    s = input()
    cnt = Counter(s)
    print(cnt.most_common(1)[0][0])

