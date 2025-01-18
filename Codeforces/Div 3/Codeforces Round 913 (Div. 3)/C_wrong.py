from collections import defaultdict
from random import *
from string import ascii_lowercase

def wrong(S):
    res1 = cal(S)
    res2 = cal(S[::-1])
 
    return min(res1, res2)
def cal(S):
    n = len(S)
    st1 = []
    i = 0
    while (i < n):
        ch = S[i]
        if len(st1) > 1 and st1[-2] == st1[-1] and st1[-1] != ch:
            st1.pop()
        elif st1 and i+1 < n and st1[-1] == ch and ch != S[i+1]:
            i += 1
        else:
            st1.append(ch)
        i += 1
    st1.reverse()
 
    st3 = []
    for ch in st1:
        if st3 and st3[-1] != ch:
            st3.pop()
        else:
            st3.append(ch)
    return len(st3)
 
def correct(S):
    N = len(S)
    ans = 0
    cnt = defaultdict(int)

    for ch in S:
        cnt[ch] += 1
        ans = max(ans, cnt[ch])
    
    if ans > N / 2:
        return 2 * ans - N
    else:
        return N % 2


S = "aaaabbbbcccc"


print(wrong(S))
print(correct(S))
exit()


RUN = 100000
for _ in range(RUN):
    N = randint(1, 100)
    S = "".join([choice(ascii_lowercase) for _ in range(N)])
    res1 = wrong(S)
    res2 = correct(S)
    if res1 != res2:
        print(S)
        print(res1, res2)
        break