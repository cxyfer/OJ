/*
 * @lc app=leetcode.cn id=2563 lang=cpp
 *
 * [2563] 统计公平数对的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
1. Sorting + Binary Search
由於順序不影響 Fair Pairs 的對數，只需要確保不重複計算即可，因此可以先對nums進行排序。

然後對於每個 i，找到有多少 j 可以使 lower <= nums[i] + nums[j] <= upper
即 lower - nums[i] <= nums[j] <= upper - nums[i]，這可以透過二分搜尋來找到。

但注意不能包含 (i, i) 這種情況，以及不能重複計算。
這可以透過限制二分的範圍在 [0, i) 或 [i + 1, n) 來解決：
或是也能先不管，但先扣掉 (i, i) 的情況後，最後再除以 2 即可。

2. Sorting + Two Pointers
使用前綴和或數學排容的思想，求 lo <= x + y <= hi 的對數，等同求 x + y <= hi 的對數減去 x + y < lo 的對數。
而如果我們能確保 x 從小枚舉到大，那麼滿足條件的 y 只會越來越小，
如此一來我們就可以使用 Two Pointers 來找到滿足條件的 y 了。
*/
// @lc code=start
class Solution1 {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        long long ans = 0;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n; ++i) {
            ans +=
                upper_bound(nums.begin(), nums.begin() + i, upper - nums[i]) -
                lower_bound(nums.begin(), nums.begin() + i, lower - nums[i]);
        }
        return ans;
    }
};
class Solution2 {
public:
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        auto f = [&](int hi) -> long long {
            long long res = 0;
            int j = n - 1;
            for (int i = 0; i < n && j > i; i++) {
                while (j > i && nums[i] + nums[j] > hi) j--;
                res += j - i;
            }
            return res;
        };
        return f(upper) - f(lower - 1);
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end