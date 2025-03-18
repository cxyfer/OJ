/*
 * @lc app=leetcode.cn id=2401 lang=cpp
 * @lcpr version=30204
 *
 * [2401] 最长优雅子数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
 *   在子陣列中，每個位元只能出現一次
 *   1. 用 cnt 來記錄每個位元出現的次數、 over 來記錄有幾個位元出現超過一次
 *   2. 用 or_val 來記錄當前每個位元是否出現過
 *   3. LogTrick
 */
// @lc code=start
class Solution1 {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int n = nums.size();
        int ans = 0, left = 0, over = 0;
        vector<int> cnt(32, 0);
        for (int right = 0; right < n; right++) {
            int x = nums[right];
            // 1. 入窗口
            while (x) {
                int lb = x & -x;
                if (++cnt[__builtin_ctz(lb)] == 2) over++;
                x ^= lb;
            }
            // 2. 出窗口
            while (over > 0) {
                int y = nums[left++];
                while (y) {
                    int lb = y & -y;
                    if (--cnt[__builtin_ctz(lb)] == 1) over--;
                    y ^= lb;
                }
            }
            // 3. 更新答案
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};

class Solution2 {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int n = nums.size();
        int ans = 0, left = 0, or_val = 0;
        for (int right = 0; right < n; right++) {
            int x = nums[right];
            // 1. 要先出窗口才能入窗口
            while (or_val & x) or_val ^= nums[left++];
            // 2. 入窗口
            or_val |= x;
            // 3. 更新答案
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};

class Solution3 {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for (int right = 0; right < n; right++) {
            int or_val = nums[right];
            int left = right - 1;
            while (left >= 0 && (or_val & nums[left]) == 0)
                or_val |= nums[left--];
            ans = max(ans, right - left);
        }
        return ans;
    }
};

class Solution : public Solution1 {};
// class Solution : public Solution2 {};
// class Solution : public Solution3 {};
// @lc code=end



/*
// @lcpr case=start
// [1,3,8,48,10]\n
// @lcpr case=end

// @lcpr case=start
// [3,1,5,11,13]\n
// @lcpr case=end

 */

