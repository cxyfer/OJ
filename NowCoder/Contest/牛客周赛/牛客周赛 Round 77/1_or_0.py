"""
    TLE
"""

class Node:
    __slots__ = ('z', 'p', 's', 'a')

    def __init__(self, z=0, p=0, s=0, a=False):
        self.z = z
        self.p = p
        self.s = s
        self.a = a

class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.s = "#" + s  # 讓 index 從 1 開始
        self.tree = [Node() for _ in range(4 * self.n)]
        self.build(1, 1, self.n)

    def build(self, o, left, right):  # node, left, right
        if left == right:  # Leaf node initialization
            if self.s[left] == '0':
                self.tree[o] = Node(z=1, p=1, s=1, a=True)
            else:
                self.tree[o] = Node(z=0, p=0, s=0, a=False)
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid)  # left child
        self.build(2*o+1, mid + 1, right)  # right child
        self.tree[o] = self.merge(
            self.tree[2*o], self.tree[2*o+1], left, mid, right)

    # 合併 [left, mid] 和 [mid+1, right] 兩部分的結果
    def merge(self, left_part, right_part, left, mid, right):
        a = (left_part.a and right_part.a)
        p = (mid - left + 1) + right_part.p if left_part.a else left_part.p
        s = (right - mid) + left_part.s if right_part.a else right_part.s
        z = left_part.z + right_part.z + left_part.s * right_part.p
        return Node(z, p, s, a)

    def query(self, o, left, right, l, r):
        if left == l and r == right:
            return self.tree[o]
        mid = (left + right) // 2
        if r <= mid:  # 只需要查詢左半部分
            return self.query(2*o, left, mid, l, r)
        if mid < l:  # 只需要查詢右半部分
            return self.query(2*o+1, mid + 1, right, l, r)
        left_part = self.query(2*o, left, mid, l, mid)
        right_part = self.query(2*o+1, mid+1, right, mid+1, r)
        return self.merge(left_part, right_part, l, mid, r)  # 合併左右兩部分

def count(L):
    return L * (L + 1) // 2

n = int(input())
s = input()
q = int(input())

st = SegmentTree(s)
for _ in range(q):
    l, r = map(int, input().split())
    ans = count(r - l + 1) - st.query(1, 1, n, l, r).z
    print(ans)