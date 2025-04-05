/*
 * @lc app=leetcode.cn id=1863 lang=cpp
 *
 * [1863] 找出所有子集的异或总和再求和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
1. Brute force + Backtracking + Bit Manipulation: O(n * 2^n)
2. Math + Bit Manipulation: O(n)

**按位考慮**，考慮每個子集中該位 1 的個數
- 若該子集中該位 1 的個數為奇數，則該位的 XOR 值為 1
- 若該子集中該位 1 的個數為偶數，則該位的 XOR 值為 0

接著考慮所有子集中該位的 XOR 和
- 若所有元素中的該位皆為 0 ，則所有 2^n 個子集中，該位的 XOR 和顯然為 0
- 若該位至少有一個 1，則有 2^(n-1) 個子集中該位 1 的個數為奇數、2^(n-1) 個子集中該位 1 的個數為偶數

證明如下：

1. 方法一：二項式定理
假設有 m 個 1，則有 n-m 個 0，故包含 k 個 1 的子集數量為 2^(n-m) * C(m, k)
而根據二項式定理，(x + 1)^m = C(m, 0) + C(m, 1) * x + C(m, 2) * x^2 + ... + C(m, m) * x^m
當 x = -1 時，(1 - 1)^m = 0 = C(m, 0) - C(m, 1) + C(m, 2) - C(m, 3) + ...
即包含偶數個 1 和包含奇數個 1 的子集數量相等，而總集合數量為 2^n
故包含偶數個 1 的子集數量為 2^(n-1)，包含奇數個 1 的子集數量亦為 2^(n-1)

2. 方法二：選或不選
假設該位有至少一個 1，則可以先取出 1 個 1，此時剩下的 n-1 個元素有 2^(n-1) 個子集，考慮這些子集
- 若該子集中有偶數個 1，則可以「選」額外的 1，此時有奇數個 1
- 若該子集中有奇數個 1，則可以「不選」額外的 1，此時有奇數個 1
也就是說，這 2^(n-1) 個子集都能透過選或不選額外的 1 來得到奇數個 1
故可以得出 2^(n-1) 個子集中該位 1 的個數為奇數

若第 i 位中至少有一個元素的該位為 1，則該位對答案的貢獻為 2^i * 2^(n-1) = (1 << i) << (n-1)
所以只要用判斷所有元素中是否有一個元素的該位為 1 即可，可以計算所有元素的 OR 值，最後左移 n-1 位即可
*/
// @lc code=start
class Solution1 {
public:
    int subsetXORSum(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        for (int i = 0; i < (1 << n); i++) {  // 枚舉所有子集，狀態壓縮
            int cur = 0;                      // 當前子集的 XOR 和
            for (int j = 0; j < n; j++)       // 當前元素是否在子集中
                if (i & (1 << j)) cur ^= nums[j];
            ans += cur;
        }
        return ans;
    }
};

class Solution2 {
public:
    int subsetXORSum(vector<int>& nums) {
        return reduce(nums.begin(), nums.end(), 0, bit_or<int>())
               << (nums.size() - 1);
    }
};

using Solution = Solution1;
// using Solution = Solution2;
// @lc code=end

