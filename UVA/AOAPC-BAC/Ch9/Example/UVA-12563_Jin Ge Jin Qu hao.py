from functools import lru_cache

# 讀取測試案例數量
t = int(input())

for kase in range(1, t + 1):
    # 讀取每組測試資料
    n, t = map(int, input().split())
    songs = list(map(int, input().split()))

    t = min(sum(songs) + 678, t)
    dp = [-1] * (t + 1) # dp[i] 表示剩餘時間 i 時能唱的最多歌曲數量
    dp[0] = 0
    for song in songs:
        for j in range(t, song - 1, -1):
            dp[j] = max(dp[j], dp[j - song] + 1)

    print(f"Case {kase}: {dp[t]} {t - dp[t] * 678}")
