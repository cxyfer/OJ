n, h, m = map(int, input().split())

st1, st2, st3 = set(), set(), set()  # 通勤、午休、臨睡

for _ in range(n):
    uid, date, time = input().split()
    uid = int(uid)

    YYYY, MM, _ = map(int, date.split('-'))
    hh, mm, ss = map(int, time.split(':'))

    t = hh * 3600 + mm * 60 + ss
    if YYYY == h and MM == m:
        if 7 * 3600 <= t <= 9 * 3600 or 18 * 3600 <= t <= 20 * 3600:  # 通勤
            st1.add(uid)
        if 11 * 3600 <= t <= 13 * 3600:  # 午休
            st2.add(uid)
        if 22 * 3600 <= t <= 24 * 3600 or 0 <= t <= 1 * 3600:  # 臨睡
            st3.add(uid)

print(len(st1), len(st2), len(st3))