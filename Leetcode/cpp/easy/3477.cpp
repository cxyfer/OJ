/*
 * @lc app=leetcode.cn id=3477 lang=cpp
 * @lcpr version=30204
 *
 * [3477] 水果成篮 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = baskets.size();
        int ans = 0;
        for (int fruit : fruits) {
            int flag = 1;
            for (int i = 0; i < n; i++) {
                if (fruit <= baskets[i]) {
                    baskets[i] = -1;
                    flag = 0;
                    break;
                }
            }
            ans += flag;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [4,2,5]\n[3,5,4]\n
// @lcpr case=end

// @lcpr case=start
// [3,6,1]\n[6,4,7]\n
// @lcpr case=end

 */

