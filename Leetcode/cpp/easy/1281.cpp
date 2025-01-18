/*
 * @lc app=leetcode id=1281 lang=cpp
 * @lcpr version=30112
 *
 * [1281] Subtract the Product and Sum of Digits of an Integer
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 100005;

class Solution {
public:
    int subtractProductAndSum(int n) {
        LL p=1, s=0, d;
        while (n > 0){
            d = n % 10;
            p *= d;
            s += d;
            n /= 10;
        }
        return (p - s);
    }
};
// @lc code=end
int main() {
    Solution sol = Solution();
    cout << sol.subtractProductAndSum(234) << endl;
    return 0;
}


/*
// @lcpr case=start
// 234\n
// @lcpr case=end

// @lcpr case=start
// 4421\n
// @lcpr case=end

 */

