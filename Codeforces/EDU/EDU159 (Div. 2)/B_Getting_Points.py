"""
    Python 會 TLE，改用 C++ AC 
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write


anss = []
T = int(input())

for tc in range(1, T+1):
    n, P, l, t = map(int, input().split())

    cnt_2t = (n + 6)// 14 # 可以讀書+完成兩份作業的天數
    cnt_1t = (n + 6) // 7  - 2 * cnt_2t # 可以讀書+完成一份作業的天數
    cnt_l = n - cnt_2t - cnt_1t # 只能夠靠讀書獲取學分的天數
    
    score = 0
    ans = n
    while score < P and ans > 0:
        if cnt_2t > 0:
            if (P - score) % (2 * t + l) == 0:
                r = (P - score) // (2 * t + l)
            else:
                r = (P - score) // (2 * t + l) + 1
            day = min(r, cnt_2t)
            score += day * (2 * t + l)
            cnt_2t -= day
            ans -= day
        elif cnt_1t > 0:
            if (P - score) % (t + l) == 0:
                r = (P - score) // (t + l)
            else:
                r = (P - score) // (t + l) + 1
            day = min(r, cnt_1t)
            score += day * (t + l)
            cnt_1t -= day
            ans -= day
        elif cnt_l > 0:
            if (P - score) % t == 0:
                r = (P - score) // l
            else:
                r = (P - score) // l + 1
            day = min(r, cnt_l)
            score += day * l
            cnt_l -= day
            ans -= day
        else:
            break
    
    anss.append(ans)

for ans in anss:
    print(f'{ans}\n')
        
