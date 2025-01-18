/*
 * @lc app=leetcode.cn id=1296 lang=cpp
 *
 * [1296] 划分数组为连续数字的集合
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) {
        map<int, int> cnt; // ordered map
        for (int x : nums) cnt[x]++;
        for (auto it = cnt.begin(); it != cnt.end(); it++) {
            if (it->second == 0) continue;
            int need = it->second;
            for (int i = 0; i < k; i++) {
                if (cnt[it->first + i] < need) return false;
                cnt[it->first + i] -= need;
            }
        }
        return true;
    }
};
// @lc code=end

