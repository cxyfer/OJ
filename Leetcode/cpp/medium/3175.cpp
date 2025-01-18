/*
 * @lc app=leetcode id=3175 lang=cpp
 *
 * [3175] Find The First Player to win K Games in a Row
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        Same as 1535. Find the Winner of an Array Game
    */
    int findWinningPlayer(vector<int>& skills, int k) {
        int n = skills.size();
        k = min(k, n);
        int ans = 0;  // index of the player wins k games
        int cnt = 0;
        for (int i = 1; i < n; i++) {
            if (skills[i] > skills[ans]) {
                ans = i;
                cnt = 0;
            }
            cnt++;
            if (cnt == k) break;
        }
        return ans;
    }
};
// @lc code=end