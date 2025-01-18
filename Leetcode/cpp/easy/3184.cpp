/*
 * @lc app=leetcode id=3184 lang=cpp
 *
 * [3184] Count Pairs That Form a Complete Day I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int countCompleteDayPairs(vector<int>& hours) {
        int n = hours.size(), ans = 0;
        for (int i = 0; i < n; i++)
            for (int j = i+1; j < n; j++)
                if ((hours[i] + hours[j]) % 24 == 0)
                    ans++;
        return ans;
    }
};
// @lc code=end