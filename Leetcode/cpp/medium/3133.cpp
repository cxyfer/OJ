/*
 * @lc app=leetcode id=3133 lang=cpp
 * @lcpr version=30122
 *
 * [3133] Minimum Array End
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
class Solution {
public:
    LL minEnd(int n, int x) {
        n -= 1;
        LL ans = x;
        int i = 0, j = 0;
        while (n) {
            if (!((ans >> i) & 1)) { // x 的第 i 位是 0，可以填充
                if ((n >> j) & 1) { // n 的第 j 位是 1，需要填充
                    ans |= (1LL << i); // 注意要用 1LL，否則 1 << i 會 overflow
                    n -= (1 << j);
                }
                j++;
            }
            i++;
        }
        return ans;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    /* code */
    Solution sol;

    cout << sol.minEnd(6715154, 7193485) << endl; // 55012476815
    return 0;
}


/*
// @lcpr case=start
// 3\n4\n
// @lcpr case=end

// @lcpr case=start
// 2\n7\n
// @lcpr case=end

 */

