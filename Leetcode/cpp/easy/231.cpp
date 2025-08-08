/*
 * @lc app=leetcode id=231 lang=cpp
 * @lcpr version=30112
 *
 * [231] Power of Two
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool isPowerOfTwo(int n) {
        // return n > 0 && __builtin_popcount(n) == 1;
        return n > 0 && (n & -n) == n;
        // return n > 0 && (n & (n - 1)) == 0;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    cout << sol.isPowerOfTwo(1) << endl; // true
    cout << sol.isPowerOfTwo(16) << endl; // true
    cout << sol.isPowerOfTwo(3) << endl; // false
    cout << sol.isPowerOfTwo(-16) << endl; // false
    return 0;
}


/*
// @lcpr case=start
// 1\n
// @lcpr case=end

// @lcpr case=start
// 16\n
// @lcpr case=end

// @lcpr case=start
// 3\n
// @lcpr case=end

 */

