"""
從小到大列舉當最大亮度為 b 時的有效區間數。
此時該位置以左(包含該位置)的星星都能作為有效的左端點，右端點同理。
有效區間為該位置以左(包含該位置)的星星數 * 該位置以右(包含該位置)的星星數。
"""
from atcoder.fenwicktree import FenwickTree

def solve1():
    N = int(input())
    B = list(map(int, input().split()))

    # 紀錄每個亮度對應的星星位置
    pos = [0] * (N + 1)
    for i, b in enumerate(B):
        pos[b] = i

    ans = 0
    bit = FenwickTree(N)
    for b in range(1, N + 1):
        idx = pos[b]
        # 將當前亮度 b 的星星位置加入 BIT
        # 此時 BIT 中存在的點都是亮度 <= b 的點
        bit.add(idx, 1)
        # 計算以當前星星為最大值的合法集合數
        ans += bit.sum(0, idx + 1) * bit.sum(idx, N)  # [l, r)
    print(ans)

def solve2():
    N = int(input())
    B = list(map(int, input().split()))
    assert len(B) == N

    ans = 0
    bit = FenwickTree(N)
    for b in B:
        # 總共有 b - 1 個亮度小於 b 的星星
        # bit 中對值域維護了左側的星星，因此左側亮度小於 b 的星星數為 bit.sum(0, b)
        left = bit.sum(0, b)
        # 右側亮度小於 b 的星星數為 (b - 1) - left
        right = b - 1 - left
        # 以當前星星為最大值的合法集合數
        ans += (left + 1) * (right + 1)
        bit.add(b - 1, 1)
    print(ans)

if __name__ == '__main__':
    # solve1()
    solve2()