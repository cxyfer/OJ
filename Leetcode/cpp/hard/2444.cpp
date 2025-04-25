/*
 * @lc app=leetcode.cn id=2444 lang=cpp
 * @lcpr version=30204
 *
 * [2444] 统计定界子数组的数目
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        int n = nums.size();
        // 分組循環，使每組的數字都滿足 minK <= nums[i] <= maxK
        int i = 0;
        vector<pair<int, int>> groups;
        while (i < n) {
            if (nums[i] < minK || nums[i] > maxK) i++;
            else {
                int st = i;
                while (i + 1 < n && nums[i+1] >= minK && nums[i+1] <= maxK) i++;
                groups.push_back({st, i});
                i++;
            }
        }
        // 對每組進行 Sliding Window
        long long ans = 0;
        for (auto [st, ed] : groups) {
            int mx = st - 1, mn = st - 1;
            for (int right = st; right <= ed; right++) {
                if (nums[right] == minK) mn = right;
                if (nums[right] == maxK) mx = right;
                int left = min(mx, mn);
                ans += left - st + 1;
            }
        }
        return ans;
    }
};

class Solution2 {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long ans = 0;
        int min_idx = -1, max_idx = -1, L = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == minK) min_idx = i;
            if (nums[i] == maxK) max_idx = i;
            if (nums[i] < minK || nums[i] > maxK) L = i + 1;
            int left = min(min_idx, max_idx);
            if (left >= L) ans += left - L + 1;
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [1,3,5,2,7,5]\n1\n5\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1,1]\n1\n1\n
// @lcpr case=end

 */

