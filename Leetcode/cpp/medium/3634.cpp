/*
 * @lc app=leetcode.cn id=3634 lang=cpp
 * @lcpr version=30204
 *
 * [3634] 使数组平衡的最少移除数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int minRemoval(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int ans = n;
        for (int i = 0; i < n; i++) {
            int j = upper_bound(nums.begin(), nums.end(), 1LL * nums[i] * k) - nums.begin();
            ans = min(ans, n - (j - i));
        }
        return ans;
    }
};

class Solution2 {
public:
    int minRemoval(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int ans = n;
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j < n && nums[j] <= 1LL * nums[i] * k) j++;
            ans = min(ans, n - (j - i));
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [2,1,5]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,6,2,9]\n3\n
// @lcpr case=end

// @lcpr case=start
// [4,6]\n2\n
// @lcpr case=end

 */

