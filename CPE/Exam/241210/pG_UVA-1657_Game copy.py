from itertools import combinations
from collections import defaultdict

while True:
    try:
        N, M = map(int, input().strip().split())
    except:
        break
    
    # 注意 s_cnt 是由 B 紀錄、p_cnt 是由 A 紀錄
    s_cnt = defaultdict(int)
    p_cnt = defaultdict(int)

    # 紀錄所有可能的 pair
    pairs = list(combinations(range(1, N+1), 2))
    for (x, y) in pairs:
        sum_ = x + y
        prod = x * y
        s_cnt[sum_] += 1
        p_cnt[prod] += 1
    
    m = len(pairs)
    used = [False] * m # 紀錄已經排除的 pair
    for i in range(1, M + 1):
        for j, (x, y) in enumerate(pairs):
            if used[j]:
                continue
            prod = x * y
            sum_ = x + y
            if i & 1:
                # A 說我不知道，但若 A 得到的 x + y = sum_ 如果只剩下一種可能的話，則 A 已經知道答案了，
                # 故顯然 A 得到的不是 x + y，可以排除這個 pair
                if s_cnt[sum_] == 1:
                    used[j] = True
                    s_cnt[sum_] -= 1
                    p_cnt[prod] -= 1
            else:
                # B 說我不知道，但若 B 得到的 x * y = prod 如果只剩下一種可能的話，則 B 已經知道答案了，
                # 故顯然 B 得到的不是 x * y，可以排除這個 pair
                if p_cnt[prod] == 1:
                    used[j] = True
                    p_cnt[prod] -= 1
                    s_cnt[sum_] -= 1

    ans = []
    for j, (x, y) in enumerate(pairs):
        if used[j]:
            continue
        if M & 1: # 最後是 A 說我知道了
            if p_cnt[x * y] == 1:
                ans.append((x, y))
        else: # 最後是 B 說我知道了
            if s_cnt[x + y] == 1:
                ans.append((x, y))
    
    ans.sort()
    print(len(ans))
    for (x, y) in ans:
        print(f"{x} {y}")