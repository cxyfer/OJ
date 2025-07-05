/*
 * @lc app=leetcode.cn id=1394 lang=cpp
 * @lcpr version=30204
 *
 * [1394] 找出数组中的幸运数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int, int> cnt;
        for (auto &x : arr) cnt[x]++;
        int ans = -1;
        for (auto &[k, v] : cnt)
            if (k == v) ans = max(ans, k);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [2,2,3,4]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,2,3,3,3]\n
// @lcpr case=end

// @lcpr case=start
// [2,2,2,3,3]\n
// @lcpr case=end

// @lcpr case=start
// [5]\n
// @lcpr case=end

// @lcpr case=start
// [7,7,7,7,7,7,7]\n
// @lcpr case=end

 */

