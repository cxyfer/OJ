"""
P1792 [国家集训队] 种树
https://www.luogu.com.cn/problem/P1792

Similar:
- P1484 种树
- 3892. Minimum Operations to Achieve At Least K Peaks
"""

# fmt: off
import sys
it = iter(sys.stdin.read().split())
def input(n: int = 1):
    return (next(it) for _ in range(n))
# fmt: on


def solve():
    n, k = map(int, input(2))
    A = list(map(int, input(n)))

    if k > n // 2:
        print("Error!")
        return

    def f(nums: list[int]) -> int:
        INF = int(1e18)
        nums = [-INF] + nums + [-INF]  # 左右邊界哨兵

        res = []
        st = []
        pp = p = None
        for v in nums:
            while pp is not None and p is not None and pp <= p >= v:  # p 是局部最大值
                res.append(p)  # 選擇 p
                v += pp - p  # 合併兩側元素 v = pp + v - p，作為反悔後的收益
                p = st.pop() if st else None
                pp = st.pop() if st else None
            if pp is not None:
                st.append(pp)
            pp, p = p, v
        res.sort(reverse=True)
        return sum(res[:k])

    print(max(f(A[:-1]), f(A[1:])))


if __name__ == "__main__":
    solve()
