/*
 * @lc app=leetcode id=2660 lang=cpp
 * @lcpr version=30112
 *
 * [2660] Determine the Winner of a Bowling Game
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
class Solution {
public:
    int isWinner(vector<int>& player1, vector<int>& player2) {
        LL f1 = f(player1), f2 = f(player2);
        if (f1 > f2) return 1;
        if (f1 < f2) return 2;
        return 0;
    }
    LL f(vector<int>& player) {
        LL res = 0;
        int pre1=0, pre2=0;
        for (auto x : player) {
            res += (pre1 || pre2)? 2*x : x;
            pre1 = pre2;
            pre2 = (x == 10)? 1 : 0;
        }
        return res;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [4,10,7,9]\n[6,5,2,3]\n
// @lcpr case=end

// @lcpr case=start
// [3,5,7,6]\n[8,10,10,2]\n
// @lcpr case=end

// @lcpr case=start
// [2,3]\n[4,1]\n
// @lcpr case=end

 */

