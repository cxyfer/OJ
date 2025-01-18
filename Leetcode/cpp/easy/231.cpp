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
        if (n <= 0) return false;
        int cnt = 0;
        while (n){
            cnt += (n & 1);
            n >>= 1;
        }
        return (cnt == 1);
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

