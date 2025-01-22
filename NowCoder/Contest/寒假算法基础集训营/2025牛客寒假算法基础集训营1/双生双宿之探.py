from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    intervals = []
    cnt = defaultdict(int)
    left = right = 0
    while right < n:
        # 擴大右端點，直到區間內有超過兩種數
        while right < n and len(cnt) <= 2:  
            cnt[A[right]] += 1
            right += 1
        # 區間內只有一種或兩種數，此時不用縮小左端點，只發生在整個陣列只有一或兩種數的情況
        if len(cnt) <= 2:  
            if len(cnt) == 2:
                intervals.append((left, right - 1))
            break
        intervals.append((left, right - 2))  # A[right - 1] 是第三種數
        # 縮小左端點，直到區間內只有兩種數
        while left < right - 1 and len(cnt) > 2:  
            cnt[A[left]] -= 1
            if cnt[A[left]] == 0:
                del cnt[A[left]]
            left += 1

    # 補上最後一個區間
    if intervals and intervals[-1][1] != n - 1 and len(cnt) == 2:
        intervals.append((left, n - 1))

    ans = 0
    for l, r in intervals:
        # 用前綴和+雜湊表計算兩個元素數量恰好相等的區間數量
        s = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        for i in range(l, r + 1):
            s += 1 if A[i] == A[l] else -1
            ans += cnt[s]
            cnt[s] += 1
    print(ans)