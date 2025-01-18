import re
from itertools import count

for kase in count(1):
    try:
        K, L = map(int, input().strip().split())
    except:
        break
    keywords = set([input().lower() for _ in range(K)])
    excuses = [input() for _ in range(L)]

    cnt = [0] * L
    for idx, excuse in enumerate(excuses):
        n = len(excuse)
        line = excuse.lower()
        words = re.split(r'[^a-z]', line)
        for word in words:
            if word in keywords:
                cnt[idx] += 1

    mx = max(cnt)
    print(f"Excuse Set #{kase}")
    for i, c in enumerate(cnt):
        if c == mx:
            print(excuses[i])
    print()