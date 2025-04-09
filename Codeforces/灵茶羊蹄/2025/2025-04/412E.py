from itertools import pairwise

"""
{pre}@{domain}.{tld}

由於一個信箱地址只能包含一個 @，因此可以先按照 @ 分割，再檢查分割後的各個部分是否合法。
"""

def check1(ch):
    return ch.isalpha() or ch.isdigit() or ch == '_'

def check2(ch):
    return ch.isalpha() or ch.isdigit()

s = input()

ans = 0
for pre, suf in pairwise(s.split('@')):
    cnt_l = cnt_r = 0
    for ch in pre[::-1]:
        if not check1(ch):
            break
        cnt_l += ch.isalpha()

    splits = suf.split('.')
    if len(splits) < 2:
        continue

    domain, tld = splits[0], splits[1]
    if any(not check2(ch) for ch in domain) or len(domain) == 0 or len(tld) == 0:
        continue

    for ch in tld:
        if not ch.isalpha():
            break
        cnt_r += ch.isalpha()
    
    ans += cnt_l * cnt_r

print(ans)