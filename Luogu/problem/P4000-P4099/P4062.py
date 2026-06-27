"""
P4062 [Code+#1] Yazid 的新生舞会
https://www.luogu.com.cn/problem/P4062
根號分治

3739. Count Subarrays With Majority Element II 的思考題，
把求給定 target 作為主要元素的子陣列數，改成不指定 target，存在任意元素做為主要元素的子陣列數。

由於出現次數 > B 的元素最多只會有 n/B 個，因此這部分可以沿用 3739 的作法，此部分為 O(n^2/B)。
對於出現次數 <= B 的元素，由於這些元素最多只能是長度為 2B-1 區間的多數元素，因此可以直接枚舉長度 < 2B 的區間，並維護出現次數最多的元素，此部分為 O(nB)。

O(n^2/B + nB) = O(n * (n/B + B))，當 B = sqrt(n) 時，時間複雜度為 O(n * sqrt(n))。
"""

from math import isqrt
from collections import defaultdict


def main():
    n, typ = map(int, input().split())
    nums = list(map(int, input().split()))

    # 保證 0 <= nums[i] < n，可以直接用陣列來存
    tot = [0] * n
    for x in nums:
        tot[x] += 1

    # 3739. Count Subarrays With Majority Element II 的 O(n) 作法
    def countMajoritySubarrays(target):
        cnt = [0] * (2 * n + 1)  # [-n, n] => [0, 2n]

        s = n  # offset 為 n，起始為 0 + offset = n
        cnt[s] = 1
        # lt = 有多少個 l 滿足 l < r 且 s[l - 1] < s[r]
        ans = lt = 0
        for x in nums:
            if x == target:
                lt += cnt[s]
                s += 1
            else:
                lt -= cnt[s - 1]
                s -= 1
            ans += lt
            cnt[s] += 1
        return ans

    B = isqrt(n) + 1
    ans = 0

    for x, v in enumerate(tot):
        if v <= B:
            continue
        ans += countMajoritySubarrays(x)

    # 枚舉長度 < 2B 的區間，並維護出現次數最多的元素
    cnt = defaultdict(int)
    for l in range(n):
        best_val, best_cnt = -1, 0
        for r in range(l, min(n, l + 2 * B - 1)):
            x = nums[r]
            cnt[x] += 1
            if cnt[x] > best_cnt:
                best_val = x
                best_cnt = cnt[x]
            # 檢查是否為多數元素，且忽略出現次數 > B 的元素
            ln = r - l + 1
            if best_cnt * 2 > ln and tot[best_val] <= B:
                ans += 1
        cnt.clear()

    print(ans)


if __name__ == "__main__":
    main()
