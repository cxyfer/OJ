"""
    Sliding Window
"""

W, B = map(int, input().split())
s = "wbwbwwbwbwbw" * 20

cnt_b = 0
for i, ch in enumerate(s): # 窗口大小為 W + B
    if i < W + B: # 還沒到窗口大小
        if ch == 'b':
            cnt_b += 1
        continue
    if cnt_b == B: # 窗口內有 B 個 b
        print("Yes")
        exit()
    if ch == 'b': # 入窗
        cnt_b += 1
    if s[i - W - B] == 'b': # 出窗
        cnt_b -= 1
print("No")