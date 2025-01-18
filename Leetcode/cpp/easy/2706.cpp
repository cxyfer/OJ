/*
 * @lc app=leetcode id=2706 lang=cpp
 * @lcpr version=30112
 *
 * [2706] Buy Two Chocolates
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
const int INF = 0x3f3f3f3f;

class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int min1 = INF, min2 = INF;
        for (auto p: prices){
            if (p < min1){
                min2 = min1;
                min1 = p;
            }else if (p < min2){
                min2 = p;
            }
        }
        return (money - min1 - min2) >= 0 ? money - min1 - min2 : money;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,2]\n3\n
// @lcpr case=end

// @lcpr case=start
// [3,2,3]\n3\n
// @lcpr case=end

 */

