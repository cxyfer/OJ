/*
 * @lc app=leetcode id=1652 lang=cpp
 * @lcpr version=30122
 *
 * [1652] Defuse the Bomb
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        if (k == 0) {
            return vector<int>(n, 0);
        }
        vector<int> ans(n, -1);
        for (int i = 0; i < n; i++) {
            int s = 0;
            if (k > 0) {
                for (int j = 1; j <= k; j++) {
                    s += code[(i+j)%n];
                }
            } else {
                for (int j = 1; j <= -k; j++) {
                    s += code[(i-j+n)%n];
                }
            }
            ans[i] = s;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [5,7,1,4]\n3\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4]\n0\n
// @lcpr case=end

// @lcpr case=start
// [2,4,9,3]\n-2\n
// @lcpr case=end

 */

