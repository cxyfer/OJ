"""
CSES-3425 Same Sum Subsets
https://cses.fi/problemset/task/3425

Meet in the Middle
"""

from collections import Counter

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    cnt = Counter(A)
    for x, v in cnt.items():
        if v > 1:  # 如果存在重複元素，則直接輸出
            print(1, x, 1, x, sep='\n')
            return

    A.sort(reverse=True)
    while A and A[0] > sum(A[1:]):  # 移除比其他全部元素相加都大的元素
        A.pop(0)

    def output(mskL, mskR):
        ansL = [x for i, x in enumerate(A) if (mskL >> i) & 1] 
        ansR = [x for i, x in enumerate(A) if (mskR >> i) & 1]
        print(len(ansL))
        print(*(ansL))
        print(len(ansR))
        print(*(ansR))

    AL, AR = [], []
    sumL = sumR = 0
    for i, x in enumerate(A):
        if sumL <= sumR:
            AL.append((i, x))
            sumL += x
        else:
            AR.append((i, x))
            sumR += x
        if sumL == sumR:
            output(sum(1 << i for i, _ in AL), sum(1 << i for i, _ in AR))
            return

    mapL, mapR = dict(), dict()
    mapL[0] = mapR[0] = 0  # (sum, mask)
    for i, x in AL:
        for s, m in mapL.items():
            if s + x in mapL:
                output(mapL[s + x], m | (1 << i))
                return
        mapL.update({s + x: m | (1 << i) for s, m in mapL.items()})
    for i, x in AR:
        for s, m in mapR.items():
            if s + x in mapR:
                output(mapR[s + x], m | (1 << i))
                return
            elif s + x in mapL:
                output(mapL[s + x], m | (1 << i))
                return
        mapR.update({s + x: m | (1 << i) for s, m in mapR.items()})
    print("IMPOSSIBLE")

if __name__ == "__main__":
    solve()