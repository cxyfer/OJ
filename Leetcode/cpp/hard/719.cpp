/*
 * @lc app=leetcode.cn id=719 lang=cpp
 *
 * [719] 找出第 K 小的数对距离
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end()); // 由小到大排序

        // 1. Binary Search
        function<int(int)> check1 = [&](int mid) { // 計算距離 <= mid 的 pair 數量
            int res = 0;
            for (int j = 0; j < n; j++) { // 枚舉右端點 j
                int i = lower_bound(nums.begin(), nums.begin() + j, nums[j] - mid) - nums.begin();
                res += j - i; // (i, j), (i+1, j), ..., (j-1, j) 距離都小於等於 mid
            }
            return res;
        };

        // 2. Sliding Window
        function<int(int)> check2 = [&](int mid) { // 計算距離 <= mid 的 pair 數量
            int res = 0, l = 0;
            for (int r = 0; r < n; r++) { // 枚舉右端點 r
                while (nums[r] - nums[l] > mid) { // 移動左端點直到滿足條件為止
                    l++;
                }
                res += r - l; // (l, r), (l+1, r), ..., (r-1, r) 距離都小於等於 mid
            }
            return res;
        };

        // 對答案做二分搜尋
        int left = 0, right = nums[n-1] - nums[0]; 
        while (left <= right) {
            int mid = left + (right - left) / 2;
            // if (check1(mid) >= k) right = mid - 1;
            if (check2(mid) >= k) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }
};
// @lc code=end