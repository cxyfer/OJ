from collections import Counter

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    S = input()

    cnt = Counter(S)
    cnt_odd = cnt_even = 0
    for v in cnt.values():
        if v % 2 == 1:
            cnt_odd += 1
        else:
            cnt_even += 1
    
    print("NO" if cnt_odd - K > 1 else "YES")