"""
D. 智乃的果子
https://ac.nowcoder.com/acm/contest/120565/D

Huffman Tree
由於會有大量的相同權重的果子，普通的做法顯然會超時，
注意到當有多個最小值時，一定是最小權重先兩兩合併，有剩餘的才會考慮其他第二小的權重。
因此額外維護相同權重的果子數量即可。
"""
from heapq import heappush, heappop

MOD = int(1e9 + 7)

def solve():
    n = int(input())
    items = [map(int, input().split()) for _ in range(n)]

    hp = []
    for c, w in items:
        heappush(hp, (w, c))
        
    ans = 0
    while len(hp) > 1 or hp[0][1] > 1:
        w, c = heappop(hp)
        while hp and hp[0][0] == w:
            c += heappop(hp)[1]

        q, r = c >> 1, c & 1
        if q > 0:
            ans += q * w * 2
            ans %= MOD
            heappush(hp, (w * 2, q))
        if r > 0:
            w2, c2 = heappop(hp)
            ans += w + w2
            ans %= MOD
            heappush(hp, (w + w2, 1))
            if c2 > 1:
                heappush(hp, (w2, c2 - 1))
    print(ans)

if __name__ == '__main__':
    solve()