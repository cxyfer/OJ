/*
 * @lc app=leetcode id=1441 lang=cpp
 * @lcpr version=30122
 *
 * [1441] Build an Array With Stack Operations
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> ans;
        int i = 1, j = 0, m = target.size();
        while (i <= n && j < m) {
            ans.push_back("Push");
            if (target[j] == i) j++;
            else ans.push_back("Pop");
            i++;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,3]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n4\n
// @lcpr case=end

 */

