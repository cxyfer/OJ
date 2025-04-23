/*
 * @lc app=leetcode.cn id=2948 lang=cpp
 * @lcpr version=30204
 *
 * [2948] 交换得到字典序最小的数组
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int n = nums.size();
        vector<int> ans(n);

        vector<pair<int, int>> A;
        for (int i = 0; i < n; i++) A.push_back({nums[i], i});
        sort(A.begin(), A.end());

        int i = 0;
        while (i < n) {
            vector<int> idxs = {A[i].second}, vals = {A[i].first};
            while (i + 1 < n && A[i + 1].first - A[i].first <= limit) {
                idxs.push_back(A[i + 1].second);
                vals.push_back(A[i + 1].first);
                i++;
            }
            sort(idxs.begin(), idxs.end());
            for (int k = 0; k < idxs.size(); k++) ans[idxs[k]] = vals[k];
            i++;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,5,3,9,8]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,7,6,18,2,1]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,7,28,19,10]\n3\n
// @lcpr case=end

 */

