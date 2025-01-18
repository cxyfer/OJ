/*
 * @lc app=leetcode id=2997 lang=cpp
 * @lcpr version=30122
 *
 * [2997] Minimum Number of Operations to Make Array XOR Equal to K
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int x = 0, ans = 0;
        for (int i: nums) {
            x ^= i;
        }
        while (x || k){
            if ((x & 1) != (k & 1)) ans++;
            x >>= 1;
            k >>= 1;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [2,1,3,4]\n1\n
// @lcpr case=end

// @lcpr case=start
// [2,0,2,0]\n0\n
// @lcpr case=end

 */

