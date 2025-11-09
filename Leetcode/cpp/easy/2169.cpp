/*
 * @lc app=leetcode.cn id=2169 lang=cpp
 * @lcpr version=30204
 *
 * [2169] 得到 0 的操作数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int countOperations(int a, int b) {
        auto f = [&](this auto&& f, int a, int b) -> int {
            return b == 0 ? 0 : a / b + f(b, a % b);
        };
        return f(a, b);
    }
};

class Solution2 {
public:
    int countOperations(int a, int b) {
        int ans = 0;
        while (b > 0) {
            ans += a / b;
            a %= b;
            swap(a, b);
        }
        return ans;
    }
};

using Solution = Solution1;
// using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// 2\n3\n
// @lcpr case=end

// @lcpr case=start
// 10\n10\n
// @lcpr case=end

 */

