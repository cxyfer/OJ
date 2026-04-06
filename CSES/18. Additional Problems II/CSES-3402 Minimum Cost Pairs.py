from itertools import accumulate


def solve():
    n = int(input())
    A = list(map(int, input().split()))

    A.sort()
    B = [abs(y - x) for x, y in zip(A[:-1], A[1:])]

    def f(nums: list[int]) -> list[int]:
        """
        回傳一個陣列 inc ，排序後前 k 個和 = 從 nums 中選 k 個不相鄰元素的最小總和

        反悔貪心
        當選擇位置為 x 的元素時，則不能選擇兩側的 L(x) 和 R(x)，
        如果要放棄原本選擇的 x，改成選擇 L(x) 或 R(x)，則反悔的代價為 val(L(x)) + val(R(x)) - val(x)。
        故可以每次選擇最小代價的元素，將其加入答案中，並將其與相鄰的元素合併。
        可以用 Doubly Linked List + Min Heap 來維護這個過程。

        然而每次取出一個元素時，他必然是局部最小值，因此也能直接用 Stack 來維護這個過程。
        """
        INF = 10**30
        nums = [INF] + nums + [INF]  # 左右邊界哨兵

        inc = []  # 收集所有「被選中的 p 值」
        st = []
        pp = p = None
        for v in nums:
            while pp is not None and p is not None and pp >= p <= v:  # p 是局部最小值
                inc.append(p)  # 選擇 p
                v += pp - p  # 合併兩側元素 v = pp + v - p，作為反悔代價
                p = st.pop() if st else None
                pp = st.pop() if st else None
            if pp is not None:
                st.append(pp)
            pp, p = p, v
        inc.sort()
        return inc

    inc = f(B)

    m = n // 2
    ans = list(accumulate(inc[:m]))
    print(*ans)


if __name__ == "__main__":
    solve()
