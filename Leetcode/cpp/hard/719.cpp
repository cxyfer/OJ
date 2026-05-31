/*
 * @lc app=leetcode.cn id=719 lang=cpp
 *
 * [719] 找出第 K 小的数对距离
 */

// @lcpr-template-start
#include <bits/stdc++.h>

#include <ranges>

using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        int n = nums.size();
        int U = ranges::max(nums) - ranges::min(nums);

        vector<int> cnt(U + 1, 0);
        for (auto [i, x] : views::enumerate(nums))
            for (int j = i + 1; j < n; ++j) ++cnt[abs(x - nums[j])];

        for (int i = 0; i <= U; ++i)
            if (k > cnt[i])
                k -= cnt[i];
            else
                return i;
        return -1;
    }
};

class Solution2 {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        int n = nums.size();
        ranges::sort(nums);

        // 計算距離 <= mid 的 pair 數量
        auto check = [&](int mid) {
            int res = 0;
            for (int j = 0; j < n; j++) {  // 枚舉右端點 j
                int i =
                    lower_bound(nums.begin(), nums.begin() + j, nums[j] - mid) -
                    nums.begin();
                res += j - i;  // [i, j) 可以做為左端點
            }
            return res;
        };

        int left = 0, right = nums[n - 1] - nums[0];
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid) >= k)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return left;
    }
};

class Solution3 {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        int n = nums.size();
        ranges::sort(nums);

        // 計算距離 <= mid 的 pair 數量
        auto check = [&](int mid) -> bool {
            int cnt = 0;
            for (int l = 0, r = 0; r < n; r++) {  // 枚舉右端點 r
                // 移動左端點直到滿足條件為止
                while (nums[r] - nums[l] > mid) {
                    l++;
                }
                cnt += r - l;  // [l, r) 可以做為左端點
            }
            return cnt >= k;
        };

        int left = 0, right = nums[n - 1] - nums[0];
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid))
                right = mid - 1;
            else
                left = mid + 1;
        }
        return left;
    }
};

// using Solution = Solution1;
// using Solution = Solution2;
using Solution = Solution3;
// @lc code=end