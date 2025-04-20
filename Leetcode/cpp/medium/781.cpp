/*
 * @lc app=leetcode.cn id=781 lang=cpp
 * @lcpr version=30204
 *
 * [781] 森林中的兔子
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numRabbits(vector<int>& answers) {
        unordered_map<int, int> cnt;
        for (int x : answers) cnt[x]++;
        int ans = 0;
        for (auto [k, v] : cnt) {
            int sz = k + 1;
            ans += sz * ((v + sz - 1) / sz);
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,1,2]\n
// @lcpr case=end

// @lcpr case=start
// [10,10,10]\n
// @lcpr case=end

 */

