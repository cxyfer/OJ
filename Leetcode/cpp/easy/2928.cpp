/*
 * @lc app=leetcode.cn id=2928 lang=cpp
 *
 * [2928] 给小朋友们分糖果 I
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int distributeCandies(int n, int limit) {
        // return solve1(n, limit);
        // return solve2(n, limit);
        return solve3(n, limit);
    }
/*
    1. Brute Force
*/
    int solve1(int n, int limit) {
        int ans = 0, k;
        for (int i = 0; i <= limit; i++) {
            for (int j = 0; j <= limit; j++) {
                k = n - i - j;
                if (k >= 0 && k <= limit) ans++;
            }
        }
        return ans;
    }
/*
    2. Optimized Brute Force
*/
    int solve2(int n, int limit) {
        int ans = 0, mx, mn;
        for (int i = 0; i <= min(limit, n); i++) {
            if (n - i > 2 * limit) continue;
            mx = min(n - i, limit); // j 的最大值
            mn = max(0, n - i - limit); // j 的最小值
            ans += mx - mn + 1;
        }
        return ans;
    }
/*
    3. 排容原理
    - 所有方案數：
        H(3, n) = C(n+2, n) = C(n+2, 2)
    - 至少一人拿到超過 limit 個糖果的方案數：
        (先分(limit+1)給他，剩下的分給所有人)
        3 * H(3, n-(limit+1)) = 3 * C(n−(limit+1)+2, 2)
    - 至少兩人拿到超過 limit 個糖果的方案數：
        3 * C(n−2⋅(limit+1)+2, 2)
*/
    int calc(int x) { // comb(x, 2)
        if (x < 0) return 0;
        return x * (x - 1) / 2;
    }
    int solve3(int n, int limit) {
        if (n > 3 * limit) return 0;
        int ans = calc(n+2); // comb(n+2, 2)
        ans -= 3 * calc(n - limit + 1);
        ans += 3 * calc(n - 2 * limit);
        // ans -= calc(n - 3 * limit - 1);
        return ans; 
    }
};
// @lc code=end

