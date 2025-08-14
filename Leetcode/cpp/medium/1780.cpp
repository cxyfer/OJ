/*
 * @lc app=leetcode.cn id=1780 lang=cpp
 * @lcpr version=30204
 *
 * [1780] 判断一个数字是否可以表示成三的幂的和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MAX_N = int(1e7 + 5);
vector<int> POW3 = {1};
auto init = []() {
    while (POW3.back() < MAX_N)
        POW3.push_back(POW3.back() * 3);
    reverse(POW3.begin(), POW3.end());
    return 0;
}();

class Solution {
public:
    bool checkPowersOfThree(int n) {
        for (int x : POW3) {
            if (n == x)
                return true;
            if (n > x)
                n -= x;
        }
        return n == 0;
    }
};
// @lc code=end



/*
// @lcpr case=start
// 12\n
// @lcpr case=end

// @lcpr case=start
// 91\n
// @lcpr case=end

// @lcpr case=start
// 21\n
// @lcpr case=end

 */

