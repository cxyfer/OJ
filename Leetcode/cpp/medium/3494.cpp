/*
 * @lc app=leetcode.cn id=3494 lang=cpp
 * @lcpr version=30204
 *
 * [3494] 酿造药水需要的最少总时间
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    long long minTime(vector<int>& skill, vector<int>& mana) {
        int n = skill.size(), m = mana.size();
        vector<long long> avail(n);
        long long t = 0;
        for (int j = 0; j < m; j++) {
            t = avail[0];
            for (int i = 0; i < n; i++)
                t = max(t, avail[i]) + skill[i] * mana[j];
            avail[n - 1] = t;
            for (int i = n - 2; i >= 0; i--)
                avail[i] = avail[i + 1] - skill[i + 1] * mana[j];
        }
        return t;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,5,2,4]\n[5,1,4,2]\n
// @lcpr case=end

// @lcpr case=start
// [1,1,1]\n[1,1,1]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4]\n[1,2]\n
// @lcpr case=end

 */

