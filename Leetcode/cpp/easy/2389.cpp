/*
 * @lc app=leetcode id=2389 lang=cpp
 * @lcpr version=30122
 *
 * [2389] Longest Subsequence With Limited Sum
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        Prefix Sum + Binary Search
    */
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size(), m = queries.size();
        sort(nums.begin(), nums.end());
        vector<int> s(n+1, 0); // prefix sum
        for (int i=0; i<n; i++) {
            s[i+1] = s[i] + nums[i];
        }
        vector<int> ans(m, 0);
        for (int i=0; i<m; i++) {
            int q = queries[i];
            ans[i] = upper_bound(s.begin(), s.end(), q) - s.begin() - 1;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [4,5,2,1]\n[3,10,21]\n
// @lcpr case=end

// @lcpr case=start
// [2,3,4,5]\n[1]\n
// @lcpr case=end

 */

