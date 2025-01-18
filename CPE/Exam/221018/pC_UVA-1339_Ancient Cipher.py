"""
    tags: APAOC-BAC-Ch4
"""
while True:
    try:
        s1 = input()
        s2 = input()
    except EOFError:
        break
    cnt1 = [0] * 26
    cnt2 = [0] * 26
    for ch in s1:
        cnt1[ord(ch) - ord('A')] += 1
    for ch in s2:
        cnt2[ord(ch) - ord('A')] += 1
    cnt1.sort()
    cnt2.sort()
    print('YES' if cnt1 == cnt2 else 'NO')
