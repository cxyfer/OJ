mp = {ch: i for i, ch in enumerate('RGBYW')}

n = int(input())
cards = list(set(map(lambda x: (mp[x[0]], int(x[1]) - 1), input().split())))  # 去重
n = len(cards)

ans = float('inf')
# 枚舉所有可能的標記方式
for msk in range(1 << 10):
    vis = set()
    # 枚舉所有卡片，根據標記方式得出這張卡片上的標記
    for card in cards:
        mark = msk & ((1 << card[0]) | (1 << (card[1] + 5)))
        vis.add(mark)
    # 若要區分所有卡片，則標記數量需要等於卡片的種類數量
    if len(vis) == n:
        ans = min(ans, msk.bit_count())
print(ans)