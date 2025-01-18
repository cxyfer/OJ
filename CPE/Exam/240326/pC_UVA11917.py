"""
    模擬(Simulation) + 雜湊表(Hash Table)
    很簡單的模擬題，只要把代寫的科目和時間存到 Hash Table 裡面，
    然後根據需要的科目判斷是否可以完成即可。
    tags: CPE-131217
"""
from collections import defaultdict

t = int(input())
for tc in range(1, t+1):
    try:
        k = int(input())
    except EOFError:
        break
    cnt = defaultdict(int)
    for _ in range(k):
        s, d = input().split()
        cnt[s] = int(d)
    n = int(input())
    target = input()
    print(f"Case {tc}: ", end="")
    if target in cnt:
        if cnt[target] <= n:
            print("Yesss")
        elif cnt[target] <= n+5:
            print("Late")
        else:
            print("Do your own homework!")
    else:
        print("Do your own homework!")