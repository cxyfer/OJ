/*
 * @lc app=leetcode.cn id=3726 lang=cpp
 * @lcpr version=30204
 *
 * [3726] 移除十进制表示中的所有零
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    long long removeZeros(long long n) {
        string s = to_string(n);
        s.erase(remove(s.begin(), s.end(), '0'), s.end());
        return stoll(s);
    }
};

class Solution2 {
public:
    long long removeZeros(long long n) {
        long long ans = 0, base = 1;
        while (n > 0) {
            int x = n % 10;
            if (x > 0) {
                ans += x * base;
                base *= 10;
            }
            n /= 10;
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// 1020030\n
// @lcpr case=end

// @lcpr case=start
// 1\n
// @lcpr case=end

 */

