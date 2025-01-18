/*
 * @lc app=leetcode.cn id=1671 lang=cpp
 *
 * [1671] 得到山形数组的最少删除次数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int minimumMountainRemovals(vector<int>& nums) {
        int n = nums.size();
        vector<int> pre(n, 1), suf(n, 1);

        // 1. Find LIS from left to right
        for (int i = 1; i < n; ++i)
            for (int j = 0; j < i; ++j)
                if (nums[i] > nums[j])
                    pre[i] = max(pre[i], pre[j] + 1);

        // 2. Find LDS from right to left
        for (int i = n - 2; i >= 0; --i)
            for (int j = n - 1; j > i; --j)
                if (nums[i] > nums[j])
                    suf[i] = max(suf[i], suf[j] + 1);

        // 3. Find the maximum length of mountain array
        int max_len = 0;
        for (int i = 1; i < n - 1; ++i)
            if (pre[i] > 1 && suf[i] > 1)
                max_len = max(max_len, pre[i] + suf[i] - 1);
        return n - max_len;
    }
};

class Solution2 {
public:
    int minimumMountainRemovals(vector<int>& nums) {
        int n = nums.size();
        vector<int> pre(n, 1), suf(n, 1);

        function<vector<int>(vector<int>&)> LIS = [&](vector<int>& nums) {
            int n = nums.size();
            vector<int> tail; // tail[i] 表示長度為 i+1 的 LIS 的最後一個元素的最小值
            vector<int> f(n); // f[i] 表示以 nums[i] 結尾的 LIS 長度
            for (int i = 0; i < n; ++i) {
                int j = lower_bound(tail.begin(), tail.end(), nums[i]) - tail.begin();
                if (j == tail.size())
                    tail.push_back(nums[i]);
                else
                    tail[j] = nums[i];
                f[i] = j + 1;
            }
            return f;
        };

        pre = LIS(nums);
        reverse(nums.begin(), nums.end()); // 反轉 nums 求 LIS
        suf = LIS(nums);
        reverse(suf.begin(), suf.end()); // 反轉 suf 恢復原狀

        int max_len = 0;
        for (int i = 1; i < n - 1; ++i)
            if (pre[i] > 1 && suf[i] > 1)
                max_len = max(max_len, pre[i] + suf[i] - 1);
        return n - max_len;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

sol = Solution();
vector<int> nums = {1, 3, 1};
cout << sol.minimumMountainRemovals(nums) << endl;
