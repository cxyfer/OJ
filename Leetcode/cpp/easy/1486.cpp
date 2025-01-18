/*
 * @lc app=leetcode id=1486 lang=cpp
 * @lcpr version=30111
 *
 * [1486] XOR Operation in an Array
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;

class Solution {
public:
    int xorOperation(int n, int start) {
        LL ans = 0;
        for (int i=0; i<n; i++) {
            ans ^= (start + i * 2);
        }
        return ans;
    }
};
// @lc code=end
int main() {
    Solution sol = Solution();
    cout << sol.xorOperation(1, 7) << endl;
    return 0;
}



/*
// @lcpr case=start
// 5\n0\n
// @lcpr case=end

// @lcpr case=start
// 4\n3\n
// @lcpr case=end

 */

